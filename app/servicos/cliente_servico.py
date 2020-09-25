from app.fabricas import db_factory
from app.models.client_entity import Cliente
import config


class ClienteServico:
    def __init__(self):
        from app.repositorios.cliente_repositorio import ClienteRepositorio
        self.__fabrica = db_factory.DbFactory(config.USER, config.PASSWORD, config.HOST,
                                              config.PORT, config.SCHEMA, config.DRIVER,
                                              config.DIALECT)
        self.__sessao = self.__fabrica.session()

        self.__cliente_repositorio = ClienteRepositorio()

    def cadastrar_cliente(self, cliente_dto):
        cliente = Cliente()

        cliente.nome_cliente = cliente_dto.nome
        cliente.dt_nascimento_cliente = cliente_dto.dt_nascimento
        cliente.email_cliente = cliente_dto.email
        cliente.senha_cliente = cliente_dto.senha

        self.__cliente_repositorio.cadastrar_cliente(cliente, self.__sessao)

    def listar_email(self, email):
        cliente_db = self.__cliente_repositorio.listar_cliente(
            email, self.__sessao)
        return cliente_db

    def deletar_cliente(self, email):
        cliente_db = self.listar_email(email)
        self.__cliente_repositorio.deletar_cliente(cliente_db, self.__sessao)
