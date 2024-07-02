from flask import Flask
from app.views import *
from app.database import test_connection

app =Flask(__name__)

#rutas de mi Api REst
app.route('/', methods=['GET'])(index)

test_connection()

if __name__=='__main__':
	app.run(debug=True)