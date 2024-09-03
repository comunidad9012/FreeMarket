from flask import Blueprint, jsonify
from models.local_model import LocalidadSchema
from schemas.localidad import Localidad
from db import db

localidad_bp=Blueprint('localidad',__name__)

@localidad_bp.route('/localidad',methods=['GET'])
def get_localidad():
    localidades=db.session.query(Localidad).all()
    localidad_schema=LocalidadSchema(many=True)
    result=localidad_schema.dump(localidades)
    return jsonify(result)