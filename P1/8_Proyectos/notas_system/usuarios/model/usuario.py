from conexionBD import conexion, cursor
import datetime
import hashlib

class Usuario:

    @staticmethod
    def hash_password(contrasena):
        return hashlib.sha256(contrasena.encode()).hexdigest()

    @staticmethod
    def registrar(nombre, apellidos, email, contrasena):
        try:
            fecha = datetime.datetime.now()
            contrasena = Usuario.hash_password(contrasena)
            sql = "INSERT INTO usuarios (nombre, apellidos, email, password, fecha) VALUES (%s, %s, %s, %s, %s)"
            val = (nombre, apellidos, email, contrasena, fecha)
            cursor.execute(sql, val)
            conexion.commit()
            return True
        except Exception as e:
            print("No se pudo registrar al usuario:", e)
            return False

    @staticmethod
    def iniciar_sesion(email, contrasena):
        try:
            contrasena = Usuario.hash_password(contrasena)
            sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"
            val = (email, contrasena)
            cursor.execute(sql, val)
            registro = cursor.fetchone()
            return registro
        except Exception as e:
            print("No se pudo iniciar sesion:", e)
            return None
