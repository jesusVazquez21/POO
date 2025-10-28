"""
Realizar un programa que conste de una clase llamada Estudiante, que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
"""
from conexionBD import *

class Estudiante:
    def __init__(self,nombre,nota):
        self._nombre=nombre
        self._nota=nota

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,nombre):
        self._nombre=nombre

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self,nota):
        self._nota=nota

    def imprimir(self):
        print(f"El alumno {self._nombre}, obtuvo una nota: {self._nota} ")

    def mostrar_nota(self):
        if self.nota>=7:
            print(f"La calificacion de la nota es: {self.nota}, si ha aprobado")
        else:
            print(f"La calificacion de la nota es: {self.nota}, No ha aprobado") 

    @staticmethod
    def insertar(nombre, nota):
                try:
                    cursor.execute(
                    "insert into estudiante values(null,%s,%s)",
                    (nombre, nota)
                    )
                    conexion.commit()
                    return True
                except:
                    return False

    @staticmethod
    def consultar():
                try:
                    cursor.execute("select * from estudiante")
                    return cursor.fetchall()
                except:    
                    return []

    @staticmethod
    def actualizar(nombre, nota, id):
                try:
                    cursor.execute(
                        "update estudiante set nombre=%s,nota=%s where id=%s",
                        (nombre, nota,id)
                    )
                    conexion.commit()
                    return True
                except: 
                    return False

    @staticmethod
    def eliminar(id):
                try:
                    cursor.execute(
                    "delete from estudiante where id=%s",
                    (id,)
                    ) 
                    conexion.commit() 
                    return True  
                except:    
                    return False

