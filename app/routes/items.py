from flask import Blueprint, request, jsonify
from flask_login import login_required,current_user
from schemas.products import ProductoSchema
from db import db
from models.producto import Producto

bp_items = Blueprint('item',__name__,url_prefix='/item')

@bp_items.post('/upload')
@login_required  
def upload_item():
    data=request.get_json()
    producto_schema=ProductoSchema(exclude=['fecha_carga_producto','estado_producto'])
    try:
        producto_data=producto_schema.load(data,session=db.session)
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    new_item=Producto(
        nombre_producto=producto_data.nombre_producto,
        descripcion_producto=producto_data.descripcion_producto,
        precio_producto=producto_data.precio_producto,
        stock_producto=producto_data.stock_producto,
        id_vendedor_producto=current_user.id_usuario,
        id_categoria_producto=producto_data.id_categoria_producto
    )
    db.session.add(new_item)
    db.session.commit()
    result=producto_schema.dump(new_item)
    return jsonify(result), 201