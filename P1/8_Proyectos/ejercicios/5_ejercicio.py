class Universidad:
    def __init__(self, nombre_uni):
        self._nombre_uni=nombre_uni

    @property
    def nombre_uni(self):
        return self._nombre_uni
    
    @nombre_uni.setter
    def nombre_uni(self, nombre_uni):
        self._nombre_uni=nombre_uni
        
class Carrera: 
    def __init__(self, especialidad):
        self._especialidad=especialidad
        
    @property
    def especialidad(self):
        return self._especialidad
    
    @especialidad.setter
    def especialidad(self, especialidad):
        self._especialidad=especialidad
        
class Estudiante(Universidad, Carrera):
    def __init__(self, nombre_uni, especialidad, nombre, edad):
        Universidad.__init__(self, nombre_uni)
        Carrera.__init__(self, especialidad)
        self._nombre=nombre
        self._edad=edad
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

persona=Estudiante("UTD", "TI", "Pepe", 19)

print(f"Nombre de alumno: ", persona.nombre, "especialidad: ", persona.especialidad, "nombre de la universidad: ", persona.nombre_uni, "edad: ", persona.edad) 