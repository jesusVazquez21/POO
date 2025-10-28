from conexionBD import *
import hashlib
import datetime

class Usuario:

    @staticmethod
    def hash_password(contrasena):
        return hashlib.sha256(contrasena.encode()).hexdigest()

    @staticmethod
    def registrar(nombre, apellidos, email, contrasena):
        try:
            contrasena = hashlib.sha256(contrasena.encode()).hexdigest()
            fecha = datetime.datetime.now()
            cursor.execute(
                "INSERT INTO usuarios VALUES (NULL, %s, %s, %s, %s, %s)",
                (nombre, apellidos, email, contrasena, fecha)
            )
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def iniciar_sesion(email, contrasena):
        try:
            contrasena = hashlib.sha256(contrasena.encode()).hexdigest()
            cursor.execute(
                "SELECT * FROM usuarios WHERE email=%s AND password=%s",
                (email, contrasena)
            )
            usuario = cursor.fetchone()
            return usuario
        except:
            return None
