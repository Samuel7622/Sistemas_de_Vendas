from abc import ABC, abstractmethod


class Pagamento(ABC):
    """Classe base para as formas de pagamento de uma venda."""

    @abstractmethod
    def calcular_valor_final(self, valor):
        """Calcula o valor final da venda para esta modalidade."""
        raise NotImplementedError


class PagamentoDebito(Pagamento):
    """Pagamento no débito, sem acréscimos ou descontos."""

    def calcular_valor_final(self, valor):
        return valor


class PagamentoPix(Pagamento):
    """Pagamento via PIX, com 5% de desconto."""

    def calcular_valor_final(self, valor):
        return valor * 0.95


class PagamentoDinheiro(Pagamento):
    """Pagamento em dinheiro, com 3% de desconto."""

    def calcular_valor_final(self, valor):
        return valor * 0.97


class PagamentoCartao(Pagamento):
    """Pagamento no cartão, com 5% de acréscimo."""

    def calcular_valor_final(self, valor):
        return valor * 1.05
