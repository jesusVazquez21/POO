from conexionBD import *
import datetime

def crear(usuario_id, titulo, descripcion,):
    try:
        sql="INSERT INTO notas (id, usuario_id, titulo, descripcion, fecha) VALUES (NULL, %s, %s, %s, NOW())"
        val=(usuario_id, titulo, descripcion)
        cursor.execute(sql, val)
        conexion.commit()
        return True
    except Exception as e:
        print("Error al crear nota:", e)
        return False
def mostrar(usuario_id):
    try:
        sql="SELECT * FROM notas where usuario_id=%s"
        val=(usuario_id,)
        cursor.execute(sql, val)
        return cursor.fetchall()
    except Exception as e:
        print("Error al cambiar nota:", e)
        return []

def cambiar(id, titulo, descripcion, usuario_id):
    try:
        # cursor.execute("SELECT id, titulo, descripcion, fecha FROM notas WHERE usuario_id = %s", (usuario_id,))
        # notas=cursor.fetchall()
        # if not notas:
        #     print("No tienes notas para modificar")
        # return False
        cursor.execute("UPDATE notas SET titulo=%s, descripcion=%s, fecha=NOW() where id=%s", (titulo, descripcion, id))
        conexion.commit()
        return True
    except:
        return False

def borrar(id):
    try:
        cursor.execute("DELETE FROM notas where id=%s", (id, ))
        conexion.commit()
        return True
    except:
        return False