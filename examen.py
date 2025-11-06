class Personas:
    def __init__(self, nombre, edad, tel):
        self.nombre=nombre
        self.edad=edad
        self.tel=tel
    

class Estudiante(Personas):
    def __init__(self, nombre, edad, tel, carrera, matricula):
        super().__init__(nombre, edad, tel)
        self.__carrera=carrera
        self.__matricula=matricula
        
        @property
        def carrera(self):
            return self.__carrera
        
        @carrera.setter
        def carrera(self, carrera):
            self.__carrera=carrera
            
            
class Docentes(Personas):
    def __init__(self, nombre, edad, tel):
        super().__init__(nombre, edad, tel) 