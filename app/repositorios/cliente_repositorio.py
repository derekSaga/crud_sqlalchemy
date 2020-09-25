from app.models.client_entity import Cliente
from sqlalchemy.exc import IntegrityError


class ClienteRepositorio:

    def cadastrar_cliente(self, cliente_bd, sessao):
        try:
            sessao.add(cliente_bd)
            sessao.commit()
        except IntegrityError as e:
            print(e)
            sessao.rollback()
        finally:
            sessao.close()

    def deletar_cliente(self, cliente_bd, sessao):
        try:
            sessao.delete(cliente_bd)
            sessao.commit()
            print("Usuario com email: %s deletado" % cliente_bd.email_cliente)
        except Exception as e:
            sessao.rollback()
            print(e)
        finally:
            sessao.close()

    def listar_cliente(self, email, sessao):
        cliente_db = sessao.query(Cliente).filter(
            Cliente.email_cliente == email).first()
        return cliente_db
