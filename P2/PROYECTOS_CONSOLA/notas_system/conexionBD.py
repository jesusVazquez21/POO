import mysql.connector


import mysql.connector

try:
    #Conectar con la BD en MySQL
    conexion=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='bd_notas'
    )
    #Crear un objeto de tipo cursor que se pueda reutilizar nuevamente
    cursor=conexion.cursor(buffered=True)
except:
     print(f"Ocurrio un error con el Sistema por favor verifique ...")    


'''
class ConexionBD:
    def __init__(self):
        try:
            #Conectar con la BD en MySQL
            self.conexion=mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='bd_notas'
            )
            #Crear un objeto de tipo cursor que se pueda reutilizar nuevamente
            self.cursor=self.conexion.cursor(buffered=True)
        except:
            print(f"Ocurrio un error con el Sistema por favor verifique ...")    


'''