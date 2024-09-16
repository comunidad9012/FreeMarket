from flask import Flask
from config import Config
from db import db, Base, login_manager
from models import provincia,localidad,categoria,usuario,direccion,producto,imagen,compra,detalle_compra,detalle_carrito
from routes.auth import bp_auth

app=Flask(__name__)
app.config.from_object(Config)

login_manager.init_app(app)
db.init_app(app)

with app.app_context():
    Base.metadata.create_all(bind=db.engine)

app.register_blueprint(bp_auth)

if __name__=='__main__':
    app.run(debug=True)
