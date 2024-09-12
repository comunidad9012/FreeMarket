from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from schemas.user import UsuarioSchema
from db import db
from models.usuario import Usuario

bp_auth = Blueprint('auth',__name__,url_prefix='/auth')

@bp_auth.post('/register')
def register():
    data=request.get_json()
    usuario_schema=UsuarioSchema(exclude=['fecha_registro_usuario'])
    try:
        usuario_data=usuario_schema.load(data,session=db.session)
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    existing_user=db.session.query(Usuario).filter_by(email_usuario=usuario_data.email_usuario).first()
    if existing_user:
        return jsonify({'error': 'El usuario ya esta registrado'}), 400
    new_user=Usuario(
        nombre_usuario=usuario_data.nombre_usuario,
        apellido_usuario=usuario_data.apellido_usuario,
        email_usuario=usuario_data.email_usuario,
        password_usuario=generate_password_hash(usuario_data.password_usuario),  
        telefono_usuario=usuario_data.telefono_usuario
    )
    db.session.add(new_user)
    db.session.commit()
    result=usuario_schema.dump(new_user)
    return jsonify(result), 201
