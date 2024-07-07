# Contiene la configuración de la base de datos
import os
from flask import g
#
from flask import Flask
from flask import request #para metodo POST
from flaskext.mysql import MySQL
#
from dotenv import load_dotenv
from flask_cors import CORS

# Cargar variables de entorno desde el archivo .env
load_dotenv()
# Inicializa nombre de mi aplicación con la aplicación Flask
app = Flask(__name__)
# Inicializa variable de tipo mysql
mysql = MySQL()

# Configuración de la base de datos usando variables de entorno
app.config['MYSQL_DATABASE_HOST']= os.getenv('MYSQL_DATABASE_HOST')
app.config['MYSQL_DATABASE_USER']=os.getenv('MYSQL_DATABASE_USER')
app.config['MYSQL_DATABASE_PASSWORD']=os.getenv('MYSQL_DATABASE_PASSWORD')
app.config['MYSQL_DATABASE_DB']=os.getenv('MYSQL_DATABASE_DB')


#-----------------------
# funcion para obtener la conexion a la base de datos
def get_db():
    # si 'database' no esta en el contexto global de flask 'g'
    if 'db' not in g:
        # crea una nueva conexion a la base de datos y la guarda en 'g'
        #g.database= psycopg2.connect(**DATABASE_CONFIG)
        g.db =mysql.connect()
    # retorna la conexion a la base de datos
    return g.db


# funcion para cerrar la conexion a la base de datos
def close_db(e=None):
    # extraer la conexion a la base de datos de 'g' y eliminarla
    db= g.pop('db', None)
    # si la conexion existe, entonces elimina la conexion
    if db is not None:
        db.close()
#-----------------------


#permitir solicitudes desde cualquier origen
CORS(app)

# Función para inicializar la aplicación con el manejo de la base de datos
def init_app(app):
    # Registrar 'close_db' para que se ejecute al final del contexto de la aplicación
    app.teardown_appcontext(close_db)


# Inicializar la base de datos con la aplicación Flask
mysql.init_app(app)    

def test_connection():
    conn =mysql.connect()
    cursor = conn.cursor()
    #conn = psycopg2.connect(**DATABASE_CONFIG)
    #conn =mysql.connect(**DATABASE_CONFIG)
    #cursor = conn.cursor()
    #cur = conn.cursor()
    conn.commit()
    cursor.close()
    conn.close()

    print("* * TEST CONECTION - OK * *")