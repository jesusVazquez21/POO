from coches import *

num_coches=int(input("Cuantos coches tienes? "))
for i in range(0, num_coches):
    
#Solictar los datos que posteriormente serán los atributos del objeto
    print=("\n\t ..::Datos del Automovil::.. {i+1}")
    marca=input("Ingresar la marca: ").upper()
    color=input("Ingresar el color: ").upper()
    modelo=input("Ingresar el modelo: ").upper()
    velocidad=int(input("Ingresa la velocidad: "))
    potencia=int(input("Ingresa la potencia: "))
    plazas=int(input("Ingresa las plazas: "))

    coche1=Coches(marca, color, modelo, velocidad, potencia, plazas)

    print(f"\n\tDatos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()} ")


















'''
coche1=Coches("VW", "Blanco", "2022", 220, 150, 5)
coche2=Coches("Nissan", "Azul", "2020", 180, 150, 6)
coche3=Coches("Honda", "", "", 0, 0, 0)
coche1.num_serie="B0123456"
coche4=Coches("", "", "", 0, 0, 0)
coche4.marca2="BMW"
print(coche4.marca)

coche3.marca2="Honda"
print(coche3.marca2)

'''

'''
print(f"Datos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()} \n Num_Serie: {coche1.num_serie} ")

print(f"Datos del Vehiculo: \n Marca:{coche2.getMarca()} \n color: {coche2.getColor()} \n Modelo: {coche2.getModelo()} \n velocidad: {coche2.getVelocidad()} \n caballaje: {coche2.getCaballaje()} \n plazas: {coche2.getPlazas()} ")

'''