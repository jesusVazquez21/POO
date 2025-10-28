"""
Realizar un programa que conste de una clase llamada Estudiante, que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
"""

class Estudiante:
    def init(self,nombre,nota):
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

estudiante1=Estudiante("Juan Porras",6)

estudiante1.imprimir()
estudiante1.mostrar_nota()