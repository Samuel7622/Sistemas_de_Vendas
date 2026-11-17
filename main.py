from Sis_vendas.pagamento import (
    PagamentoCartao,
    PagamentoDebito,
    PagamentoDinheiro,
    PagamentoPix,
)
from Sis_vendas.produto import Produto
from Sis_vendas.venda import Venda


def formatar_moeda(valor):
    """Formata um valor para o padrão brasileiro de moeda."""
    return f"R$ {valor:.2f}"


def exibir_produtos(produtos):
    """Exibe a lista de produtos e seus dados."""
    print("\n===== PRODUTOS =====")
    for produto in produtos:
        print(f"\n{produto.descricao}")
        print(f"Preço: {formatar_moeda(produto.preco_unitario)}")
        print(f"Estoque: {produto.estoque}")


def exibir_itens_venda(venda):
    """Exibe os itens da venda."""
    print("\n===== ITENS DA VENDA =====")
    if not venda.itens:
        print("Nenhum item na venda.")
        return

    for item in venda.itens:
        plural = "unidade" if item.quantidade == 1 else "unidades"
        print(
            f"{item.produto.descricao} | {item.quantidade} {plural} | "
            f"{formatar_moeda(item.calcular_subtotal())}"
        )

    print(f"\nTOTAL: {formatar_moeda(venda.valor_total)}")


def exibir_estoque_final(produtos):
    """Exibe o estoque final de cada produto."""
    print("\n===== ESTOQUE APÓS VENDA =====")
    for produto in produtos:
        print(f"{produto.descricao}: {produto.estoque}")


def testar_modalidades_pagamento():
    """Demonstra o cálculo polimórfico das quatro formas de pagamento."""
    modalidades = (
        ("Débito", PagamentoDebito(), 100.00),
        ("PIX", PagamentoPix(), 95.00),
        ("Dinheiro", PagamentoDinheiro(), 97.00),
        ("Cartão", PagamentoCartao(), 105.00),
    )

    print("\n===== TESTE DAS MODALIDADES DE PAGAMENTO =====")
    for nome, pagamento, esperado in modalidades:
        produto = Produto("Produto de teste", 100.00, 1)
        venda = Venda(pagamento)
        if not venda.adicionar_item(produto, 1):
            raise AssertionError(f"Não foi possível adicionar produto para {nome}.")
        print(f"{nome}: {formatar_moeda(venda.valor_total)}")
        assert round(venda.valor_total, 2) == esperado


def main():
    print("\n" + "=" * 50)
    print("SISTEMA DE VENDAS - TESTES")
    print("=" * 50)

    teclado = Produto("Teclado", 100.00, 10)
    mouse = Produto("Mouse", 50.00, 20)
    monitor = Produto("Monitor", 800.00, 5)
    produtos = [teclado, mouse, monitor]

    exibir_produtos(produtos)

    # O débito mantém o comportamento original de Venda() sem modalidade explícita.
    venda = Venda(PagamentoDebito())
    print("\n===== CRIANDO VENDA =====")

    print("\nAdicionando 2 Teclados...")
    print("Adicionado com sucesso." if venda.adicionar_item(teclado, 2) else "Erro ao adicionar.")

    print("\nAdicionando 3 Mouses...")
    print("Adicionado com sucesso." if venda.adicionar_item(mouse, 3) else "Erro ao adicionar.")

    print("\nAdicionando 1 Monitor...")
    print("Adicionado com sucesso." if venda.adicionar_item(monitor, 1) else "Erro ao adicionar.")

    exibir_itens_venda(venda)
    exibir_estoque_final(produtos)

    print("\n===== TESTE DE ESTOQUE INSUFICIENTE =====")
    print("\nTentando adicionar 20 Monitores...")
    print("Adicionado com sucesso." if venda.adicionar_item(monitor, 20) else "Estoque insuficiente.")

    print("\n===== REMOVENDO ITEM =====")
    print("\nRemovendo Monitor...")
    if venda.remover_item(monitor):
        print("Monitor removido com sucesso.")
        print(f"\nNovo total: {formatar_moeda(venda.valor_total)}")
        print(f"Estoque do Monitor: {monitor.estoque}")
    else:
        print("Monitor não encontrado na venda.")

    print("\n===== TESTE: REMOVER PRODUTO NÃO PRESENTE =====")
    print("\nTentando remover Monitor novamente...")
    print("Monitor removido com sucesso." if venda.remover_item(monitor) else "Monitor não está na venda.")

    print("\n===== ESTADO FINAL =====")
    exibir_itens_venda(venda)
    exibir_estoque_final(produtos)
    testar_modalidades_pagamento()

    print("\n" + "=" * 50)
    print("FIM DOS TESTES")
    print("=" * 50 + "\n")


if __name__ == "__main__":
    main()
