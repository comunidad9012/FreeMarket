from sqlalchemy import Column, Integer, String, DECIMAL, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db import Base
from schemas.usuario import Usuario
from schemas.categoria import Categoria

class Producto(Base):
    __tablename__='producto'

    id_producto=Column(Integer,primary_key=True,autoincrement=True)
    nombre_producto=Column(String(50),nullable=False)
    descripcion_producto=Column(String(250),nullable=False)
    precio_producto=Column(DECIMAL(15,0),nullable=False)
    stock_producto=Column(Integer,nullable=False)
    fecha_carga_producto=Column(DateTime,nullable=False)
    estado_producto=Column(Integer,nullable=False)
    id_vendedor_producto=Column(Integer,ForeignKey('usuario.id_usuario'),nullable=False)
    id_categoria_producto=Column(Integer,ForeignKey('categoria.id_categoria'),nullable=False)

    vendedor=relationship('Usuario',back_populates='productos')
    categoria=relationship('Categoria',back_populates='productos')
    imagenes=relationship('Imagen',back_populates='producto')
    detalles_compra=relationship('DetalleCompra',back_populates='producto')
    detalles_carrito=relationship('DetalleCarrito',back_populates='producto')