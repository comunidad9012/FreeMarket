from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from db import Base

class Usuario(Base, UserMixin):
    __tablename__='usuario'

    id_usuario=Column(Integer,primary_key=True,autoincrement=True)
    nombre_usuario=Column(String(60),nullable=False)
    apellido_usuario=Column(String(60),nullable=False)
    email_usuario=Column(String(100),nullable=False)
    password_usuario=Column(String(40),nullable=False)
    telefono_usuario=Column(Integer,nullable=False)
    fecha_registro_usuario=Column(Date,nullable=False)
    
    direcciones=relationship('Direccion',back_populates='usuario')
    productos=relationship('Producto',back_populates='vendedor')
    compras=relationship('Compra',back_populates='usuario')
    carritos=relationship('Carrito',back_populates='usuario')