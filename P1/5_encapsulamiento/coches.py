'''
Ejercicio Practico 3
'''
import os
os.system("cls")

class Coches:

    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #valores iniciales es posible declarar al principio de una clase
    #Método Constructor para incializar los valores de los atributos a la hora de 
    #crear o instanciar un objeto por primera vez de la clase
    
    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas):
        self.__marca=marca
        self.__color=color
        self.__modelo=modelo
        self.__velocidad=velocidad
        self.__caballaje=caballaje
        self.__plazas=plazas

    #Metodos o acciones o funciones que hace el objeto 
    '''
    Crear los métodos getter y setter, estos métodos son importantes y ncesarios en todas las clases 
    para que el programador interactue con los valores de los atributos a traves de estos métodos. 
    Digamos que es la manera más adecuada y recomendada para solicitar un valor (get) 
    y/o para ingresar o cambiar un valor (set) a un atributo en particular de la clase a traves de un objeto.
    
    En teoria se debería de crear un método getters y setters por cada atributo que contenga la clase
    Los métodos get siempre regresan valor, es decir el valor de la propoedad a traves del return
    por otro lado el método set siempre recive parametros para cambiar o modificar el valor 
    del atributo o proiedad en cuestion
    '''
    
    #Primera Forma
    def getMarca(self):
        return self.__marca
    
    def setMarca(self, marca):
        self.__marca=marca
    
    #Segunda Forma
    @property
    def marca2(self):
        return self.marca
    
    @marca2.setter
    def marca2(self, marca):
        self.marca=marca
    
    
    def getColor(self):
        return self.__color
    
    def setColor(self, color):
        self.__color=color
    
    def getModelo(self):
        return self.__modelo
    
    def setModelo(self, modelo):
        self.__modelo=modelo
    
    def getVelocidad(self):
        return self.__velocidad
    
    def setVelocidad(self, velocidad):
        self.__velocidad=velocidad
    
    def getCaballaje(self):
        return self.__caballaje
    
    def setCaballaje(self, caballaje):
        self.c__aballaje=caballaje
    
    def getPlazas(self):
        return self.__plazas
    
    def setPlazas(self, plazas):
        self.__plazas=plazas
    
    
    
    def acelerar(self):
        return "Estas acelerando"

    def frenar(self):
        return "Estas frenando"

#Fin definir clase

#Crear un objetos o instanciar la clase

