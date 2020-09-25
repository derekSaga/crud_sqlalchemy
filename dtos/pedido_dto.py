class PedidoDto:
    def __init__(self, dt_compra, produtos, cliente):
        self.__dt_compra = dt_compra
        self.__produtos = produtos
        self.__cliente = cliente

    @property
    def dt_compra(self):
        return self.__dt_compra

    @dt_compra.setter
    def dt_compra(self, dt_compra):
        self.__dt_compra = dt_compra

    @property
    def produtos(self):
        return self.__produtos

    @produtos.setter
    def produtos(self, produtos):
        self.__produtos = produtos

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente
