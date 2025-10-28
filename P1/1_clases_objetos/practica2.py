"""
Ejercicio Practico #2 "Modelar y Diagramar en POO"
"""
import os
os.system("cls")

class Coches:
    #Método constructor que inicializa los valores de los atributos cuando se le instancia un objeto
    def __init__(self, color, marca, velocidad):
        self.color=color
        self.marca=marca
        self.velocidad=velocidad
    
    def acelerar(self, incremento):
        self.velocidad=self.velocidad+incremento
        return self.velocidad
    
    def frenar(self, decremento):
        self.velocidad=self.velocidad-decremento
        return self.velocidad
    
    def tocar_claxon(self):
        return "*sonido de claxon*"
    
#Distanciar objetos de la clase Coches



coche1=Coches("Blanco" , "Toyota", 220)
coche2=Coches("Amarillo", "Nissan", 180)




# print(f"Los valores del objeto 1  son: {coche1.color}, {coche1.marca}, {coche1.velocidad}")
# velocidad=coche1.acelerar(50)
# print(f"La velocidad original del coche 1 es: {coche1.velocidad}, Y cambió a {velocidad}")


# print(f"Los valores del obbjeto 1  son: {coche2.color}, {coche2.marca}, {coche2.velocidad}")
# print(f"Los valores del obbjeto 1  son: {coche2.velocidad}, cambió a: {coche2.frenar(100)}")



#Que no haya método constructor
#Que todos los atributos sean públicos
#Que los métodos de acelerar y frenar no hagan nada 