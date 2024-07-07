#define los modelos de datos que se implementaran en la aplicación

from app.database import get_db


# cuando construya un nuevo objeto Users pedira todos estos datos
class Users:
    def __init__(self, idusuarios=None, nombre_apellido=None, password=None, primera_conexion=None, ultima_conexion=None, foto_perfil=None, perfil=None, estado=None):
        self.idusuarios = idusuarios
        self.nombre_apellido = nombre_apellido
        self.password = password
        self.primera_conexion = primera_conexion
        self.ultima_conexion = ultima_conexion
        self.foto_perfil = foto_perfil
        self.perfil= perfil
        self.estado= estado
        #save(self)

    @staticmethod
    def get_users_all():
        return Users.__get_users_by_query(""" SELECT * FROM usuarios
                                            ORDER BY idusuarios DESC""")
    
    #------------------
    #--- consulta usuarios por id
    @staticmethod
    def get_users_estado_true():
        return Users.__get_users_by_query
    (
    """ SELECT * FROM usuarios WHERE estado = true 
    ORDER BY idusuarios DESC"""
    )
 
    #------------------
    #--- consulta usuarios eliminados logico
    @staticmethod
    def get_users_estado_false():
        return Users.__get_users_by_query
    (
    """ SELECT * FROM usuarios WHERE estado = false
    ORDER BY idusuarios DESC"""
    )

    #------------------
    #--- consulta usuarios por id
    @staticmethod
    def get_by_id(idusuarios):
        db = get_db() # conecto a db (funcion viene de database.py)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM tareas WHERE id = %s", (idusuarios,))
        row = cursor.fetchone() # me devuelve un dato y guardo resultado en variable
        cursor.close()
        if row: # si el usuario existe, devuelvo el usuario
            return Users( idusuarios=row[0], nombre_apellido=row[1], password=row[2],
                        primera_conexion=row[3], ultima_conexion=row[4], foto_perfil=row[5], perfil=row[6], estado=row[7] )
        return None # si ek usuario no existe, no devuelvo nada

    #------------------
    #--- delete/ update
    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.idusuarios: # Actualizar Tarea existente
            cursor.execute("""UPDATE usuarios
                            SET nombre_apellido = %s, password = %s, foto_perfil = %s
                            WHERE idusuarios = %s""",
                            (self.nombre_apellido, self.password, self.foto_perfil, self.idusuarios))
        else: # Crear Tarea nueva
            cursor.execute(
                """INSERT INTO usuariosCompras
                (nombre_apellido, password, primera_conexion, ultima_conexion, foto_perfil, perfil, estado)
                VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                (self.nombre_apellido, self.password, self.primera_conexion, self.ultima_conexion, self.foto_perfil, self.perfil, self.estado))
            
            cursor.execute(
                """INSERT INTO usuariosTrasacciones
                (nombre_apellido, password, primera_conexion, ultima_conexion, foto_perfil, perfil, estado)
                VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                (self.nombre_apellido, self.password, self.primera_conexion, self.ultima_conexion, self.foto_perfil, self.perfil, self.estado))
            self.idusuarios= cursor.lastrowid
        db.commit()
        cursor.close()

    #------------------
    #--- funcion ejecuta cualquier query que le pase como parametro
    @staticmethod
    def __get_users_by_query(query):
        db= get_db() # conecto a db (funcion viene de database.py)
        cursor= db.cursor()
        cursor.execute(query)
        rows= cursor.fetchall() # me devuelve todo y guardo resultados en lista
        user= [] # creo array
        for row in rows: # recorro lista y voy almacenando cada fila y posicion
            return user( idusuarios=row[0], nombre_apellido=row[1], password=row[2],
                        primera_conexion=row[3], ultima_conexion=row[4], foto_perfil=row[5], perfil=row[6], estado=row[7] )
        cursor.close()
        return user
    
    #------------------
    #--- serialización para conversión a jsonify (si fuera necesario)
    def serialize(self):
        return {'idusuarios': self.idusuarios,
        'nombre_apellido': self.nombre_apellido,
        'password': self.password,
        'primera_conexion': self.primera_conexion('%Y-%m-%d'),
        'ultima_conexion': self.ultima_conexion('%Y-%m-%d'),
        'foto_perfil': self.foto_perfil,
        'perfil': self.perfil,
        'estado': self.estado
        }
 