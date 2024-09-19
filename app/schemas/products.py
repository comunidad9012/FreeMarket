from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from models.producto import Producto

class ProductoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model=Producto
        load_instance=True
        include_fk=True

    id_producto=fields.Int(dump_only=True)
    nombre_producto=fields.Str(required=True)
    descripcion_producto=fields.Str(required=True)
    precio_producto=fields.Decimal(required=True)
    stock_producto=fields.Int(required=True)
    estado_producto=fields.Int(required=True)
    id_vendedor_producto=fields.Int(load_only=True)
    id_categoria_producto=fields.Int(required=True)