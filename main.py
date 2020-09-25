from app.servicos.cliente_servico import ClienteServico
from app.dtos.cliente_dto import ClienteDto

if __name__ == "__main__":
    cliente_servico = ClienteServico()

    cliente = ClienteDto('derek', 'email@teste.com.br',
                         'jurubeba', '1994-06-04', 44466688899)

    cliente_db = cliente_servico.listar_email(cliente.email)

    cliente_servico.deletar_cliente(cliente_db.email_cliente)
