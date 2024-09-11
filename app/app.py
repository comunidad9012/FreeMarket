from flask import Flask
from config import Config
from db import db, Base
from models import provincia,localidad,categoria,usuario,direccion,producto,imagen,compra,detalle_compra,detalle_carrito

app=Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    Base.metadata.create_all(bind=db.engine)

if __name__=='__main__':
    app.run(debug=True)
