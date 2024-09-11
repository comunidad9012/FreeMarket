from sqlalchemy import Column, Integer, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from db import Base
from models.carrito import Carrito
from models.producto import Producto

class DetalleCarrito(Base):
    __tablename__='detalle_carrito'

    id_carrito_detalle_carrito=Column(Integer,ForeignKey('carrito.id_carrito'),primary_key=True)
    id_producto_detalle_carrito=Column(Integer,ForeignKey('producto.id_producto'),primary_key=True)
    cantidad_detalle_carrito=Column(Integer,nullable=False)
    precio_detalle_carrito=Column(DECIMAL(15,0),nullable=False)

    carrito=relationship('Carrito',back_populates='detalles_carrito')
    producto=relationship('Producto',back_populates='detalles_carrito')