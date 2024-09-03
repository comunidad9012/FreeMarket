from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from schemas.localidad import Localidad

class LocalidadSchema(SQLAlchemyAutoSchema):
    class Meta:
        model=Localidad
        load_instance=True
        
    id_localidad=fields.Int()
    id_provincia_localidad=fields.Int()
    nombre_localidad=fields.Str()