'''
Ejercicio Practico 3
'''
import os
os.system("cls")

class Coches:
    def __init__(self,marca,color,modelo,velocidad,caballaje,plazas):
        self._marca=marca
        self._color=color
        self._modelo=modelo
        self._velocidad=velocidad
        self._caballaje=caballaje
        self._plazas=plazas

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
    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self, marca):
        self._marca=marca
        
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        self._color=color
        
    @property
    def modelo(self):
        return self._modelo
    
    @modelo.setter
    def modelo(self, modelo):
        self._modelo=modelo
        
    @property
    def velocidad(self):
        return self._velocidad
    
    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad=velocidad
    
    @property
    def caballaje(self):
        return self._caballaje
    
    @caballaje.setter
    def caballaje(self, caballaje):
        self._caballaje=caballaje
    
    @property
    def plazas(self):
        return self._plazas
    
    @plazas.setter
    def plazas(self, plazas):
        self._plazas=plazas
    
    
    def acelerar(self):
        return "Estas acelerando"

    def frenar(self):
        return "Estas frenando"

class Camiones(Coches):
    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga):
        super().__init__(marca, color, modelo, velocidad, caballaje, plazas)
        self.__eje=eje
        self.__capacidadCarga=capacidadCarga
        
    def cargar(self, tipo_carga):
        self.tipo_carga=tipo_carga
        return self.tipo_carga
        
        
    def acelerar(self):
        return "Esta acelerando el camión"
    def frenar(self):
        return "Estas frenando el camión"
    
    @property
    def eje(self):
        return self.__eje
    
    @eje.setter
    def eje(self, eje):
        self.__eje=eje

    @property
    def capacidadCarga(self):
        return self.__capacidadCarga
        
    @eje.setter
    def eje(self, capacidadCarga):
        self.__capacidadCarga=capacidadCarga
        
class Camionetas(Coches):
    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrdada):
        super().__init__(marca, color, modelo, velocidad, caballaje, plazas)
        self.__traccion=traccion
        self.__cerrada=cerrdada
        
    def num_pasajeros(self, num_pasajeros):
        self.num_pasajeros=num_pasajeros
        return self.num_pasajeros
        
        
    def acelerar(self):
        return "Esta acelerando la camioneta"
    def frenar(self):
        return "Estas frenando la camioneta"
    
    @property
    def traccion(self):
        return self.__traccion
    
    @traccion.setter
    def traccion(self, traccion):
        self.__traccion=traccion

    @property
    def cerrada(self):
        return self.__cerrada
        
    @cerrada.setter
    def cerrada(self, cerrada):
        self.__cerrada=cerrada
        
        
        
coche=Coches("VW","Blanco","2022",220,150,5)
print(coche.color, coche.acelerar())
        
camion=Camiones("VW","Blanco Perlado","2022",220,150,5, 2, 2500)
print(camion.color, camion.acelerar())
        
camioneta=Camionetas("VW","Verde","2022",220,150,5, "Delantera", True)
print(camion.color, camion.acelerar())

#Fin definir clase

#Crear un objetos o instanciar la clase
""" 
coche1=Coches("VW","Blanco","2022",220,150,5)
coche2=Coches("Nissan","Azul","2020",180,150,6)
coche3=Coches("Honda","","",0,0,5)


print(f"Datos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()} ")

print(f"Datos del Vehiculo: \n Marca:{coche2.getMarca()} \n color: {coche2.getColor()} \n Modelo: {coche2.getModelo()} \n velocidad: {coche2.getVelocidad()} \n caballaje: {coche2.getCaballaje()} \n plazas: {coche2.getPlazas()} ")

coche3.marca2="Honda"
print(coche3.marca2) """



'''

class Coches:
    marca = ""
    color = ""
    modelo = ""
    velocidad = 0
    caballaje = 0
    piezas = 0
    
    def acelerar(self):
        pass
    def frenars(self):
        pass
    
coche1 = Coches()
coche1.marca = "BMW"
coche1.color = "Blanco"
coche1.modelo = "2022"
coche1.velocidad= "220"
coche1.caballaje= "150"
coche1.piezas= "5"

coche2 = Coches()
coche2.marca = "Nissan"
coche2.color= "Azul"
coche2.modelo = "2020"
coche2.velocidad = "180"
coche2.caballaje= "150"
coche2.piezas = "6"

print("=== Coche 1 ===")
print("Marca:", coche1.marca)
print("Color:", coche1.color)
print("Modelo:", coche1.modelo)
print("Velocidad:", coche1.velocidad)
print("Caballaje:", coche1.caballaje)
print("Piezas:", coche1.piezas)

print("\n=== Coche 2 ===")
print("Marca:", coche2.marca)
print("Color:", coche2.color)
print("Modelo:", coche2.modelo)
print("Velocidad:", coche2.velocidad)
print("Caballaje:", coche2.caballaje)
print("Piezas:", coche2.piezas)


'''