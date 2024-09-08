from flask import Flask
from config import Config
from db import db, Base
from schemas.provincia import Provincia
from schemas.localidad import Localidad
from schemas.categoria import Categoria
from schemas.usuario import Usuario
from schemas.direccion import Direccion
from schemas.producto import Producto
from schemas.imagen import Imagen
from schemas.compra import Compra
from schemas.detalle_compra import DetalleCompra
from schemas.carrito import Carrito
from schemas.detalle_carrito import DetalleCarrito

app=Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    Base.metadata.create_all(bind=db.engine)

if __name__=='__main__':
    app.run(debug=True)
