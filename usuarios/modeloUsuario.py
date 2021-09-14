
import database.config as conexoion

connect=conexoion.conectar()
database=connect[0]
cursor=connect[1]

class Usuario:
    def __init__(self,nombre,apellidos,email,password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password
    # Guarda lo usuarios de un 
    def guardar(self):
        # conecion para guardar 
        sql="INSERT INTO usuarios VALUE (null,%s,%s,%s,%s,now())"
        # variables que se guardaran
        usuario=(self.nombre,self.apellidos,self.email,self.password)
        # conectsor para el sql
        cursor.execute(sql,usuario)
        # actuliza la base de datos
        database.commit()
        # retorna el nombre  de usurio gurdado
        return f'Bienvenido {self.nombre}  ya estas registrado'
    # validar el email ingresado por el usuario
    def validar(email):
        # busca el Usuario en espesifico
        sql=f'SELECT * FROM usuarios WHERE email="{email}"'
        cursor.execute(sql)
        # devuelve el ressultado encontrado con toda la informacion
        result=cursor.fetchall()
        return result