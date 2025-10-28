'''
Ejercicio Practico #3 "Modelar y Diagramar en POO"
'''
import os
os.system("cls")


class Alumnos:
    def __init__(self, nombre, edad, matricula):
        self._nombre=nombre
        self._edad=edad
        self._matricula=matricula
    
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre=nombre
    
    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, edad):
        self._edad=edad
    
    @property
    def matricula(self):
        return self._matricula
    @matricula.setter
    def matricula(self, matricula):
        self._matricula=matricula
        
    def inscribirse(self):
        pass
    def estudiar(self):
        pass
    
# Instancias de Alumnos
alumno1 = Alumnos("Juan", "18", "das123")
alumno2 = Alumnos("Pepe", "19", "pep123")
alumno3 = Alumnos("Dani", "19", "dan123")

# Imprimir datos usando propiedades
print("=== DATOS DE ALUMNOS ===")
print(f"Datos del Alumno 1: \n Nombre: {alumno1.nombre} \n Edad: {alumno1.edad} \n Matricula: {alumno1.matricula}")
print("\n" + "="*50 + "\n")
 

class Profesores:
    def __init__(self, nombre, experiencia, num_profesor):
        self._nombre = nombre
        self._experiencia = experiencia
        self._num_profesor = num_profesor
        
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
        
    @property
    def experiencia(self):
        return self._experiencia
    
    @experiencia.setter
    def experiencia(self, experiencia):
        self._experiencia = experiencia
        
    @property
    def num_profesor(self):
        return self._num_profesor
    
    @num_profesor.setter
    def num_profesor(self, num_profesor):
        self._num_profesor = num_profesor
        
    def impartir(self):
        pass
    def evaluar(self):
        pass
    
# Instancias de Profesores
profesor1 = Profesores("Daniel", "10 años", "2")
profesor2 = Profesores("Rodrigo", "15 años", "3")
profesor3 = Profesores("Oscar", "10 años", "4")

print("=== DATOS DEL PROFESOR ===")
print(f"Datos del PROFESOR 1: \n Nombre: {profesor1.nombre} \n Experiencia: {profesor1.experiencia} \n Num_profesor: {profesor1.num_profesor}")
print("\n" + "="*50 + "\n")


class Cursos:
    def __init__(self, nombre, codigo, creditos):
        self._nombre=nombre
        self._codigo=codigo
        self._creditos=creditos
        
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre=nombre
        
    @property
    def codigo(self):
        return self._codigo
    @codigo.setter
    def codigo(self, codigo):
        self._codigo=codigo
    
    @property
    def creditos(self):
        return self._creditos
    @creditos.setter
    def creditos(self, creditos):
        self._creditos=creditos   
    
    def asignar(self):
        pass
    
# Instancias de Cursos
curso1 = Cursos("Matemáticas", "MAT101", "5")
curso2 = Cursos("Programación", "PROG201", "6")
curso3 = Cursos("Física", "FIS301", "4")

print("=== DATOS DEL CURSO ===")
print(f"Datos del CURSO 1: \n Nombre: {curso1.nombre} \n Codigo: {curso1.codigo} \n Creditos: {curso1.creditos}")
print("\n" + "="*50 + "\n")