from flask import Blueprint, jsonify
from models.prov_model import ProvinciaSchema
from schemas.provincia import Provincia
from db import db

provincia_bp=Blueprint('provincia',__name__)

@provincia_bp.route('/provincias',methods=['GET'])
def get_provincias():
    provincias=db.session.query(Provincia).all()
    provincia_schema=ProvinciaSchema(many=True)
    result=provincia_schema.dump(provincias)
    return jsonify(result)