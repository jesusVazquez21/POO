from conexionBD import conexion, cursor

class Autos:
    @staticmethod
    def insertar(marca, color, modelo, velocidad, caballaje, plazas):
        try:
            sql = "INSERT INTO coches VALUES(null,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, (marca, color, modelo, velocidad, caballaje, plazas))
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    @staticmethod
    def consultar():
        try:
            cursor.execute("SELECT * FROM coches")
            return cursor.fetchall()
        except:
            return []

    @staticmethod
    def buscar(id_coche):
        try:
            cursor.execute("SELECT * FROM coches WHERE id_coche=%s", (id_coche,))
            return cursor.fetchone()
        except:
            return None

    @staticmethod
    def actualizar(id_coche, marca, color, modelo, velocidad, caballaje, plazas):
        try:
            sql = "UPDATE coches SET marca=%s, color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s WHERE id_coche=%s"
            cursor.execute(sql, (marca, color, modelo, velocidad, caballaje, plazas, id_coche))
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def eliminar(id_coche):
        try:
            cursor.execute("DELETE FROM coches WHERE id_coche=%s", (id_coche,))
            conexion.commit()
            return True
        except:
            return False

class Camionetas:
    @staticmethod
    def insertar(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada):
        try:
            sql = "INSERT INTO camionetas VALUES(null,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, (marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada))
            conexion.commit()
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def consultar():
        try:
            cursor.execute("SELECT * FROM camionetas")
            return cursor.fetchall()
        except:
            return []
    
    @staticmethod
    def buscar(id_camioneta):
        try:
            cursor.execute("SELECT * FROM camionetas WHERE id_camioneta=%s", (id_camioneta,))
            return cursor.fetchone()
        except:
            return None
    
    @staticmethod
    def actualizar(marca,color,modelo,velocidad,caballaje,plazas, traccion, cerrada, id_camioneta):
        try:
            sql = "update camionetas set marca=%s, color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s,traccion=%s, cerrada=%s where id_camioneta=%s"
            cursor.execute(sql, (marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada, id_camioneta))
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def eliminar(id_camioneta):
        try:
            cursor.execute("DELETE FROM camioneta WHERE id_camioneta=%s", (id_camioneta,))
            conexion.commit()
            return True
        except:
            return False
    

class Camiones:
    @staticmethod
    def insertar(marca, color, modelo, velocidad, caballaje, plazas, eje, carga):
        try:
            sql = "INSERT INTO camiones VALUES(null,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, (marca, color, modelo, velocidad, caballaje, plazas, eje, carga))
            conexion.commit()
            return True
        except:
            return False
            
    @staticmethod
    def consultar():
        try:
            cursor.execute("SELECT * FROM camiones")
            return cursor.fetchall()
        except:
            return []
    
    @staticmethod
    def buscar(id_camion):
        try:
            cursor.execute("SELECT * FROM camiones WHERE id_camion=%s", (id_camion,))
            return cursor.fetchone()
        except:
            return None
    
    @staticmethod
    def actualizar(marca,color,modelo,velocidad,caballaje,plazas, eje, capacidadCarga, id_camion):
        try:
            sql = "update camiones set marca=%s, color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s, eje=%s, capacidadCarga=%s where id_camion=%s"
            cursor.execute(sql, (marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga, id_camion))
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def eliminar(id_camion):
        try:
            cursor.execute("DELETE FROM camioneta WHERE id_camion=%s", (id_camion,))
            conexion.commit()
            return True
        except:
            return False