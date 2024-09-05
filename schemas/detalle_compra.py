from sqlalchemy import Column, Integer, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from db import Base
from schemas.compra import Compra
from schemas.producto import Producto

class DetalleCompra(Base):
    __tablename__='detalle_compra'

    id_compra_detalle_compra=Column(Integer,ForeignKey('compra.id_compra'),primary_key=True)
    id_producto_detalle_compra=Column(Integer,ForeignKey('producto.id_producto'),primary_key=True)
    cantidad_detalle_compra=Column(Integer,nullable=False)
    precio_detalle_compra=Column(DECIMAL(15,0),nullable=False)

    compra=relationship('Compra',back_populates='detalles_compra')
    producto=relationship('Producto',back_populates='detalles_compra')