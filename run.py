from flask import Flask
from app.views import *
from app.database import *
from flask_cors import CORS

app =Flask(__name__)

# ruta funcion de la vista -> devuelve mensaje en json
app.route('/', methods=['GET'])(index)

# ruta funcion de la vista -> consulta usuarios
app.route('/api/users/all', methods=['GET'])(get_view_users_all)

# ruta de funcion de la vista -> consulta user por id
app.route('/api/users/byid/<int:users_id>', methods=['GET'])(get_users_byid)

# ruta de funcion de la vista -> crea usuario mediante post
app.route('/api/users/create/', methods=['POST'])(create_new_user)

# ruta de funcion de la vista -> actualiza usuario mediante post
app.route('/api/users/update/<int:users_id>', methods=['PUT'])(update_users_byid)

# funcion de prueba de conexion a la base de datos
#test_connection()

init_app(app)
#permitir solicitudes desde cualquier origen
CORS(app)

if __name__=='__main__':
	app.run(debug=True)