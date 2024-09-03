from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class Categoria(Base):
    __tablename__='categoria'

    id_categoria=Column(Integer,primary_key=True,autoincrement=True)
    nombre_categoria=Column(String(50),nullable=False)
    id_main_categoria=Column(Integer,ForeignKey('categoria.id_categoria'))

    main_categoria=relationship('Categoria',remote_side=[id_categoria],backref='subcategorias')
    productos=relationship('Producto',back_populates='categoria')