from Sis_vendas.pagamento import (
    PagamentoCartao,
    PagamentoDebito,
    PagamentoDinheiro,
    PagamentoPix,
)
from Sis_vendas.produto import Produto
from Sis_vendas.venda import Venda


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
        if round(venda.valor_total, 2) != esperado:
            raise AssertionError(f"Valor incorreto para {nome}: {venda.valor_total}")
        print(f"{nome}: R$ {venda.valor_total:.2f}")


if __name__ == "__main__":
    testar_modalidades_pagamento()
