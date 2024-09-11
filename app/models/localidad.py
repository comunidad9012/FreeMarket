from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base
from models.provincia import Provincia

class Localidad(Base):
    __tablename__='localidad'

    id_localidad=Column(Integer,primary_key=True,autoincrement=True)
    id_provincia_localidad=Column(Integer,ForeignKey('provincia.id_provincia'),nullable=False)
    nombre_localidad=Column(String(100),nullable=False)

    provincia=relationship('Provincia',back_populates='localidades')
    direcciones=relationship('Direccion',back_populates='localidad')