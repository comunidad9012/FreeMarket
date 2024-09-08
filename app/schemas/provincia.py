from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db import Base

class Provincia(Base):
    __tablename__='provincia'

    id_provincia=Column(Integer,primary_key=True,autoincrement=True)
    nombre_provincia=Column(String(75),nullable=False)

    localidades=relationship('Localidad',back_populates='provincia')