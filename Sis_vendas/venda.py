from datetime import datetime

if __package__:
    from .item_venda import ItemVenda
    from .pagamento import PagamentoDebito
else:
    from item_venda import ItemVenda
    from pagamento import PagamentoDebito


class Venda:
    """Classe que representa uma venda com múltiplos itens."""

    def __init__(self, pagamento=None):
        self.__data = datetime.now()
        self.__valor_total = 0.0
        self.__itens = []
        # Mantém a compatibilidade com chamadas antigas como Venda().
        self.__pagamento = pagamento if pagamento is not None else PagamentoDebito()

    @property
    def data(self):
        """Retorna a data da venda."""
        return self.__data

    @property
    def valor_total(self):
        """Retorna o valor final da venda, já considerando o pagamento."""
        return self.__valor_total

    @property
    def itens(self):
        """Retorna a lista de itens da venda."""
        return self.__itens

    @property
    def pagamento(self):
        """Retorna a forma de pagamento da venda."""
        return self.__pagamento

    def adicionar_item(self, produto, quant):
        """Adiciona um item à venda.

        Args:
            produto (Produto): produto a adicionar
            quant (int): quantidade a adicionar

        Returns:
            bool: True se conseguiu adicionar, False caso contrário
        """
        if quant <= 0:
            return False

        # Tenta decrementar o estoque do produto
        if not produto.decrementar_estoque(quant):
            return False

        # Cria um item de venda com o preço atual do produto
        item = ItemVenda(produto, quant, produto.preco_unitario)
        self.__itens.append(item)

        # Recalcula o total
        self.calcular_total()

        return True

    def remover_item(self, produto):
        """Remove um item da venda.

        Args:
            produto (Produto): produto a remover

        Returns:
            bool: True se conseguiu remover, False caso contrário
        """
        for i in range(len(self.__itens)):
            if self.__itens[i].produto == produto:
                # Pega o item que será removido
                item = self.__itens[i]

                # Devolve a quantidade ao estoque
                produto.incrementar_estoque(item.quantidade)

                # Remove da lista
                self.__itens.pop(i)

                # Recalcula o total
                self.calcular_total()

                return True

        return False

    def calcular_total(self):
        """Calcula o total dos itens e aplica a forma de pagamento.

        Returns:
            float: valor final da venda
        """
        subtotal = sum(item.calcular_subtotal() for item in self.__itens)
        self.__valor_total = self.__pagamento.calcular_valor_final(subtotal)
        return self.__valor_total
