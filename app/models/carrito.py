from sqlalchemy import Column, Integer, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from db import Base
from models.usuario import Usuario

class Carrito(Base):
    __tablename__='carrito'

    id_carrito=Column(Integer,primary_key=True)
    id_usuario_carrito=Column(Integer,ForeignKey('usuario.id_usuario'),nullable=False)
    fecha_carrito=Column(DateTime,nullable=False)
    estado_carrito=Column(Boolean,nullable=False)

    usuario=relationship('Usuario',back_populates='carritos')
    detalles_carrito=relationship('DetalleCarrito',back_populates='carrito')
