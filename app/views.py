#define las rutas y la logica de negocio de la aplicacion

# jsonify define json a partir de objetos python
from flask import jsonify

def index():

    #devuelve json de datos como api
    return jsonify({
        'mensaje': 'Hello World APIS con FLASK'})
    #las llaves hablan de diccionario