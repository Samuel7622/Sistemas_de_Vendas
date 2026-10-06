from .produto import Produto


class ItemVenda:
    """Classe que representa um item dentro de uma venda."""
    
    def __init__(self, produto, quantidade, valor_item):
        self.__produto = produto
        self.__quantidade = quantidade
        self.__valor_item = valor_item
    
    @property
    def produto(self):
        """Retorna o produto do item."""
        return self.__produto
    
    @property
    def quantidade(self):
        """Retorna a quantidade do item."""
        return self.__quantidade
    
    @property
    def valor_item(self):
        """Retorna o valor unitário do item."""
        return self.__valor_item
    
    def calcular_subtotal(self):
        """Calcula o subtotal do item (quantidade * valor_item).
        
        Returns:
            float: subtotal do item
        """
        return self.__quantidade * self.__valor_item
