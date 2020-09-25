class ProdutoDto:
    def __init__(self, nome_produto, preco):
        self.__nome_produto = nome_produto
        self.__preco = preco

    @property
    def nome_produto(self):
        return self.__nome_produto

    @nome_produto.setter
    def nome_produto(self, nome_produto):
        self.__nome_produto = nome_produto

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        self.__preco = preco
