class Produto:
    """Classe que representa um produto no estoque."""
    
    def __init__(self, descricao, preco_unitario, estoque):
        self.__descricao = descricao
        self.__preco_unitario = preco_unitario
        self.__estoque = estoque
    
    @property
    def descricao(self):
        """Retorna a descrição do produto."""
        return self.__descricao
    
    @property
    def preco_unitario(self):
        """Retorna o preço unitário do produto."""
        return self.__preco_unitario
    
    @property
    def estoque(self):
        """Retorna a quantidade em estoque."""
        return self.__estoque
    
    def decrementar_estoque(self, quant):
        """Diminui o estoque do produto.
        
        Args:
            quant (int): quantidade a decrementar
            
        Returns:
            bool: True se conseguiu decrementar, False caso contrário
        """
        if quant <= 0:
            return False
        
        if quant > self.__estoque:
            return False
        
        self.__estoque -= quant
        return True
    
    def incrementar_estoque(self, quant):
        """Aumenta o estoque do produto.
        
        Args:
            quant (int): quantidade a incrementar
        """
        if quant > 0:
            self.__estoque += quant
