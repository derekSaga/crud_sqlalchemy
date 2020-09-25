from app.dtos.cliente_dto import ClienteDto
from app.servicos.cliente_servico import ClienteServico

if __name__ == "__main__":
    cliente_servico = ClienteServico()

    cliente = ClienteDto('derek', 'derek.coelho@outlook.com.br',
                         'jurubeba', '1994-06-04')

    cliente_db = cliente_servico.listar_email(cliente.email)

    cliente_servico.deletar_cliente(cliente_db.email_cliente)
