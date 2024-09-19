from flask import Blueprint, jsonify
from models.producto import Producto
from schemas.products import ProductoSchema
from db import db

bp_home=Blueprint('home',__name__)

@bp_home.get('/')
def show_list():
    list=db.session.query(Producto).all()
    producto_schema=ProductoSchema(many=True)
    result=producto_schema.dump(list)
    return jsonify(result)