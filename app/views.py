#define las rutas y la logica de negocio de la aplicacion

# jsonify define json a partir de objetos python
from flask import jsonify, request
from app.models import Users
from datetime import date

# -------------- test de conexión a la base de datos ----------------
# ----
# 
def index():

    #devuelve json de datos como api
    return jsonify({
        'mensaje': 'Hello World APIS con FLASK'})
    #las llaves hablan de diccionario

# -------------- recibe petición get, devuelve usuarios en base de datos  ----------------
# ----
# 
def get_users(): 
    # los corchetes son listas
    # las llaves son diccionarios
    users = [
        {
            'idusuarios':1,
            'nombre_aplellido':'Nombre Apellido 1',
            'password':'1234',
            'primera_conexion': '2024-06-01',
            'ultima_conexion':  '2024-06-15',
            'foto_perfil': 'perfil1.png',
            'perfil': 'usuario',
            'estado' : 'activo'
        },
        {
            'idusuarios':2,
            'nombre_aplellido':'Nombre Apellido 2',
            'password':'12345',
            'primera_conexion':  '2024-01-01',
            'ultima_conexion':  '2024-06-30',
            'foto_perfil': 'perfil2.png',
            'perfil': 'administrador',
            'estado' : 'activo'
        }
    ]
    return jsonify(users) 

# -------------- recibe id devuelve usuarios por id en base de datos  ----------------
# ----
# 
def get_users_byid(users_id):
 users = {
 'idusuario': users_id,
 }
 return jsonify(users)

# -------------- recibe peticion request, toma datos recibidos  ----------------
# ---- crea nuevo users
# 
def create_new_user():
 #datos recibidos en formato json
    data = request.json
    new_user = Users(
        nombre_apellido=data['nombre_apellido'],
        password=data['password'],
        primera_conexion=date.today().strftime('%Y-%m-%d'),
        ultima_conexion=date.today().strftime('%Y-%m-%d'),
        foto_perfil=data['foto_perfil'],
        perfil=data['perfil'],
        estado=data['estado']
    )
    new_user.save()
    return jsonify({'message': 'User created successfully'}), 201

# -------------- recibe peticion request, toma datos recibidos  ----------------
# ---- actualiza users
# 
def update_users_byid(users_id):
 #datos recibidos en formato json
 data = request.json
 return jsonify({'message': 'User updated successfully','data':data,'idusuario':users_id})


# --------------  ----------------
# ---- 
# 
def get_view_users_all():
    users = Users.get_users_all()
    return jsonify([users.serialize() for user in users])

def get_view_users_estado_true():
    users = Users.get_users_estado_true()
    return jsonify([users.serialize() for user in users])

def get_view_users_estado_false():
    users = Users.get_users_estado_false()
    return jsonify([users.serialize() for user in users])

# --------------  ----------------
# ---- 
# 