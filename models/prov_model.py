from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from schemas.provincia import Provincia

class ProvinciaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model=Provincia
        load_instance=True
        
    id_provincia=fields.Int()
    nombre_provincia=fields.Str()