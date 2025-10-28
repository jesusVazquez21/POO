import mysql.connector

try:
    conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="bd_notas"
    )
    cursor = conexion.cursor(buffered=True)
except:
    print("No fue posible conectarse a la Base de Datos. Inténtelo más tarde...")
