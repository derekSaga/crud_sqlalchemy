from sqlalchemy.sql.schema import Column, Table
from sqlalchemy.sql.sqltypes import DECIMAL, Date, Float, String
from sqlalchemy.types import Integer
from sqlalchemy_utils import PasswordType
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

produto_pedido = Table('produto_pedido', Base.metadata,
                       Column('produto_id', Integer,
                              ForeignKey('produto.id_produto')),
                       Column('pedido_id', Integer,
                              ForeignKey('pedido.id_pedido'))
                       )


class Cliente(Base):
    __tablename__ = 'cliente'

    id_cliente = Column(Integer, primary_key=True, autoincrement=True)
    nome_cliente = Column(String(100), nullable=False)
    email_cliente = Column(String(150), nullable=False, unique=True)
    senha_cliente = Column(PasswordType(max_length=256, schemes=[
        'pbkdf2_sha512',
        'md5_crypt'
    ]), nullable=False)
    dt_nascimento_cliente = Column(Date, nullable=False)
    doc_cliente = Column(DECIMAL(11), unique=True, nullable=False)
    pedidos = relationship('Pedido', back_populates='cliente')


class Produto(Base):
    __tablename__ = 'produto'

    id_produto = Column(Integer, primary_key=True, autoincrement=True)
    nome_produto = Column(String(150), nullable=False)
    preco = Column(Float, nullable=False)

    pedidos = relationship(
        'Pedido', back_populates='produtos', secondary='produto_pedido')


class Pedido(Base):
    __tablename__ = 'pedido'

    id_pedido = Column(Integer, primary_key=True, autoincrement=True)
    dt_compra = Column(Date, nullable=False)
    cliente_id = Column(Integer, ForeignKey('cliente.id_cliente'))

    produtos = relationship(
        'Produto', back_populates="pedidos", secondary='produto_pedido')
    cliente = relationship('Cliente', back_populates='pedidos')

# Base.metadata.create_all(engine)
