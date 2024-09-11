from sqlalchemy import Column, Integer, DateTime, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from db import Base
from models.usuario import Usuario

class Compra(Base):
    __tablename__='compra'

    id_compra=Column(Integer,primary_key=True,autoincrement=True)
    id_usuario_compra=Column(Integer,ForeignKey('usuario.id_usuario'),nullable=False)
    fecha_compra=Column(DateTime,nullable=False)
    total_compra=Column(DECIMAL(15,0),nullable=False)

    usuario=relationship('Usuario',back_populates='compras')
    detalles_compra=relationship('DetalleCompra',back_populates='compra')