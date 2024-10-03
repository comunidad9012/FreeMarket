from flask import Flask
from flask_cors import CORS
from config import Config
from db import db, Base, login_manager
from models import provincia,localidad,categoria,usuario,direccion,producto,imagen,compra,detalle_compra,detalle_carrito
from routes.auth import bp_auth
from routes.items import bp_items
from routes.home import bp_home

app=Flask(__name__)
app.config.from_object(Config)
CORS(app)

login_manager.init_app(app)
db.init_app(app)

with app.app_context():
    Base.metadata.create_all(bind=db.engine)

app.register_blueprint(bp_auth)
app.register_blueprint(bp_items)
app.register_blueprint(bp_home)

if __name__=='__main__':
    app.run(host="0.0.0.0",debug=True)
