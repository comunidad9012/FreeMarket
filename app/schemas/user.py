from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from models.usuario import Usuario

class UsuarioSchema(SQLAlchemyAutoSchema):
    class Meta:
        model=Usuario
        load_instance=True

    id_usuario=fields.Int(dump_only=True)
    nombre_usuario=fields.Str(required=True)
    apellido_usuario=fields.Str(required=True)
    email_usuario=fields.Email(required=True)
    password_usuario=fields.Str(required=True) #ver cositas de seguridad con esta linea
    telefono_usuario=fields.Int(required=True)
