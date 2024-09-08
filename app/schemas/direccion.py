from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base
from schemas.usuario import Usuario
from schemas.localidad import Localidad

class Direccion(Base):
    __tablename__='direccion'

    id_direccion=Column(Integer,primary_key=True,autoincrement=True)
    id_usuario_direccion=Column(Integer,ForeignKey('usuario.id_usuario'),nullable=False)
    id_localidad_direccion=Column(Integer,ForeignKey('localidad.id_localidad'),nullable=False)
    calle_direccion=Column(String(50),nullable=False)
    numero_direccion=Column(Integer,nullable=False)
    codigo_postal_direccion=Column(Integer,nullable=False)

    usuario=relationship('Usuario',back_populates='direcciones')
    localidad=relationship('Localidad',back_populates='direcciones')