from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base
from schemas.producto import Producto

class Imagen(Base):
    __tablename__='imagen'

    id_imagen=Column(Integer,primary_key=True,autoincrement=True)
    url_imagen=Column(String(100),nullable=False)
    id_producto_imagen=Column(Integer,ForeignKey('producto.id_producto'),nullable=False)

    producto=relationship('Producto',back_populates='imagenes')