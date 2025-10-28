import os 
os.system("cls")

class Clase:
    atributo_publico="Soy un atributo publico"
    _atributo_protegido="Soy un atributo protegido"
    __atributo_privado="Soy un atributo privado"
    
    def __init__(self, color, tamano, ):
        self.__color=color
        self.__tamano=tamano
        
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color):
        self.__color=color

    @property
    def tamano(self):
        return self.__tamano
    @tamano.setter
    def color(self, tamano):
        self.__tamano=tamano
        
        
    
    def getAtributoPrivado(self):
        return self.__atributo_privado
    
    def __getAtributoPrivado(self):
        self.__getAtributoPrivado()
    
    def getAtributoPrivado2(self):
        self.__getAtributoPrivado()
    
    def setAtributoPrivado(self, atributo_privado):
        self.__atributo_privado=atributo_privado
    
    #Usar los atributos y métodos de acuerdo a su encapsulamiento
objeto=Clase("Rojo", "Grande")
print(f"Mi objeto tiene los siguientes atributos: {objeto.color}, {objeto.tamano}")



print(f"Soy el contenido del atributo publico: {objeto.atributo_publico}")
print(f"Soy el contenido del atrbuto protegido: {objeto._atributo_protegido}")
print(f"Soy el contenido del atributo privado: {objeto.getAtributoPrivado()}")
objeto.setAtributoPrivado("Se ha cambiado el valor del atributo privado")
print(f"Soy el contenido del atributo privado: {objeto.getAtributoPrivado()}")