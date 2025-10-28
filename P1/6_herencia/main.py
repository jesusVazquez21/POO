from Coches import *
import os
#Solicitar los datos que posteriormente seran los atributs del objeto




def autos():
    num_coches = int(input("Cuantos coches tiene?"))
    for i in range(0,num_coches):
        print("Datos del auto")
        marca = input("Marca: ").upper()
        color = input("Color: ").upper()
        modelo = input("Modelo: ").upper()
        velocidad = int(input("Velocidad: ").upper())
        potencia = int(input("Potencia: ").upper())
        plazas = int(input("Plazas: ").upper())
        coche1 = Coches(marca,color,modelo,velocidad,potencia,plazas)
        
    coche1=Coches(marca, color, modelo, velocidad, potencia, plazas)
        
    print(f"Datos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()} ")

def camionetaa():
    print("Datos del vehiculo")
    marca = input("Marca: ").upper()
    color = input("Color: ").upper()
    modelo = input("Modelo: ").upper()
    velocidad = int(input("Velocidad: ").upper())
    potencia = int(input("Potencia: ").upper())
    plazas = int(input("Plazas: ").upper())
    traccion=input("Ingresar el tipo de traccion: ").upper()
    cerrada=input("Ingresar SI/NO si es cerrada o no: ").upper()
    if cerrada=="SI":
        cerrada=True
    else:
        cerrada=False


    coche1=Camionetas(marca, color, modelo, velocidad, potencia, plazas, traccion, cerrada)

    print(f"Datos del Vehiculo: \n Marca:{coche1.marca()} \n color: {coche1.color()} \n Modelo: {coche1.modelo()} \n velocidad: {coche1.velocidad()} \n caballaje: {coche1.caballaje()} \n plazas: {coche1.plazas()} ")




opcion=1
while opcion!=4:
    os.system("cls")
    print("..:: MENU PRINCIPAL ::..")
    opcion=input("\n\t 1.- Autos \n\t 2.- Camionetas\n\t 3.- Camiones\n\t 4.- Salir\n\t Elige una opción: ").lower().strip()
    match opcion: 
        case "1": 
            print("Autos")
            input("Oprima tecla para continuar")
        case "2":
            print("Camionetas")
            input("Oprima tecla para continuar")
        case "3":
            print("Camiones")
            input("Oprima tecla para continuar")
        case "4":
            print("Salir")
            input("Oprima tecla para continuar")
        case _:
            print("Opción Invalida..... Vuelva a intentarlo")
            input("Oprima tecla para continuar")  








''' 
num_coches = int(input("Cuantos coches tiene?"))
for i in range(0,num_coches):
    print("Datos del auto")
    marca = input("Marca: ").upper()
    color = input("Color: ").upper()
    modelo = input("Modelo: ").upper()
    velocidad = int(input("Velocidad: ").upper())
    potencia = int(input("Potencia: ").upper())
    plazas = int(input("Plazas: ").upper())
    coche = Coches(marca,color,modelo,velocidad,potencia,plazas)

'''