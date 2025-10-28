from conexionBD import conexion, cursor
import datetime

class Nota:
    @staticmethod
    def crear (usuario_id, titulo, descripcion):
        try:
            sql="insert into notas (usuario_id, titulo, descripcion, fecha) VALUES (%s, %s, %s, NOW())"
            val=(usuario_id, titulo, descripcion)
            cursor.execute(sql, val)
            conexion.commit
            True
        except Exception as e:
            print(f"No se pudo crear la nota: ", {e})
            False
            
    @staticmethod
    def mostrar(usuario_id):
        try:
            sql="select * from notas where usuario_id=%s"
            val=(usuario_id, )
            cursor.execute(sql, val)
            return cursor.fetchall()
        except Exception as e:
            print(f"No se pudo mostrar las notas: ", {e})
            return False
    
    @staticmethod
    def actualizar(id_nota, titulo, descripcion):
        try:
            sql="update notas set titulo=%s, descripcion=%s, fecha=NOW() where id_nota=%s"
            val=(titulo, descripcion, id_nota)
            cursor.execute(sql, val)
            conexion.commit
            return True
        except Exception as e:
            print(f"No se pudo actualizar la nota: ", {e})
            return False
        
    @staticmethod
    def borrar(id_nota):
        try:
            sql = "DELETE FROM notas WHERE id = %s"
            val = (id_nota)
            cursor.execute(sql, val)
            conexion.commit()
            return True
        except Exception as e:
            print("No se pudo borrar la nota:", e)
            return False