import unittest

from Sis_vendas.pagamento import (
    PagamentoCartao,
    PagamentoDebito,
    PagamentoDinheiro,
    PagamentoPix,
)
from Sis_vendas.produto import Produto
from Sis_vendas.venda import Venda


class TestPagamentoVenda(unittest.TestCase):
    def test_valores_finais_das_modalidades(self):
        casos = (
            (PagamentoDebito(), 100.00),
            (PagamentoPix(), 95.00),
            (PagamentoDinheiro(), 97.00),
            (PagamentoCartao(), 105.00),
        )

        for pagamento, valor_esperado in casos:
            with self.subTest(pagamento=type(pagamento).__name__):
                produto = Produto("Produto de teste", 100.00, 1)
                venda = Venda(pagamento)
                self.assertTrue(venda.adicionar_item(produto, 1))
                self.assertAlmostEqual(venda.valor_total, valor_esperado, places=2)

    def test_venda_sem_pagamento_mantem_debito_por_compatibilidade(self):
        produto = Produto("Produto de teste", 100.00, 1)
        venda = Venda()

        self.assertTrue(venda.adicionar_item(produto, 1))
        self.assertEqual(venda.valor_total, 100.00)
        self.assertIsInstance(venda.pagamento, PagamentoDebito)


if __name__ == "__main__":
    unittest.main()
