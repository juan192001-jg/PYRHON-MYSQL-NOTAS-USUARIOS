from mysql.connector import connect
import database.config as conexoion

connect=conexoion.conectar()
database=connect[0]
cursor=connect[1]

class Notas:
    # costructor
    def __init__(self,usuario_id,titulo,descripcion):
        self.usuario_id = usuario_id
        self.titulo =titulo
        self.descripcion=descripcion
    # guardar un nueva nota
    def guardar(self):
        sql="INSERT INTO notas VALUE (null,%s,%s,%s,now())"
        notas=(self.usuario_id,self.titulo,self.descripcion)
        cursor.execute(sql,notas)
        database.commit()
        return f'La nota {self.titulo} se a Gurdado corectamente'
    # busca la noto por el titulo
    def buscarTitilo(titulo):
        sql = f'SELECT * FROM notas WHERE titulo="{titulo}"'
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    # busca todas la notas
    def buscarTodo():
        sql = 'SELECT * FROM notas'
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    # elimina la nota que tenga el titulo ingrseado por el suario
    def eliminarNota(titulo):
        sql = f'DELETE FROM notas WHERE titulo="{titulo}"'
        cursor.execute(sql)
        database.commit()
        return f'la nota {titulo} se elimino con exito'
    