from Sis_vendas.pagamento import PagamentoDebito
from Sis_vendas.produto import Produto
from Sis_vendas.venda import Venda


def testar_modalidades_pagamento():
    """Demonstra o cálculo polimórfico das quatro formas de pagamento."""
    modalidades = [
        ("Débito", PagamentoDebito()),
        ("PIX", PagamentoPix()),
        ("Dinheiro", PagamentoDinheiro()),
        ("Cartão", PagamentoCartao()),
    ]

    print("\n===== TESTE DAS MODALIDADES DE PAGAMENTO =====")
    for nome, pagamento in modalidades:
        produto = Produto("Produto de teste", 100.00, 1)
        venda = Venda(pagamento)
        if not venda.adicionar_item(produto, 1):
            raise AssertionError(f"Não foi possível adicionar produto para {nome}.")
        print(f"{nome}: R$ {venda.valor_total:.2f}")


# Imports locais para permitir executar este arquivo como script.
try:
    from Sis_vendas.pagamento import PagamentoPix, PagamentoDinheiro, PagamentoCartao
except ModuleNotFoundError:
    from pagamento import PagamentoPix, PagamentoDinheiro, PagamentoCartao


if __name__ == "__main__":
    testar_modalidades_pagamento()
