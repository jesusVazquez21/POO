#Instanciar los objetos para posterior implementarlos 
from coches import *
import os

def datos_autos(tipo):
    print(f"\n\t ...Ingresar los datos del Vehiculo de tipo: {tipo}")
    marca=input("Marca: ").upper()
    color=input("Color: ").upper()
    modelo=input("Modelo: ").upper()
    velocidad=int(input("Velocidad: "))
    potencia=int(input("Potencia: "))
    plazas=int(input("No. de plazas: "))
    return marca, color, modelo, velocidad, potencia, plazas

def imprimir_datos_vehiculo(marca, color, modelo, velocidad, potencia, plazas):
    print(f"\n\tDatos del Vehiculo: \n Marca:{marca} \n color: {color} \n Modelo: {modelo} \n velocidad: {velocidad} \n caballaje: {potencia} \n plazas: {plazas}")

def autos():
    marca,color,modelo,velocidad,potencia,plazas=datos_autos("Auto")
    coche=Coches(marca, color, modelo, velocidad, potencia, plazas)
    imprimir_datos_vehiculo(coche.marca, coche.color, coche.modelo, coche.velocidad, coche.caballaje, coche.plazas)

def camionetas():
    marca,color,modelo,velocidad,potencia,plazas=datos_autos("Camioneta")
    traccion=input("Traccion: ").upper()
    cerrada=input("¿Cerrada (Si/No)?: ").upper().strip()
    if cerrada=="SI":
        cerrada=True
    else:
        cerrada=False    
    coche=Camionetas(marca, color, modelo, velocidad, potencia, plazas, traccion, cerrada)
    imprimir_datos_vehiculo(coche.marca, coche.color, coche.modelo, coche.velocidad, coche.caballaje, coche.plazas)
    print(f"traccion: {coche.traccion}\n cerrada: {coche.cerrada}")

def camiones():
    marca,color,modelo,velocidad,potencia,plazas=datos_autos("Camiones")
    eje=int(input("No. de ejes: "))
    capacidadCarga=int(input("Capacidad de carga: "))
    coche=Camiones(marca,color,modelo,velocidad,potencia,plazas,eje,capacidadCarga)
    imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
    print(f"#Ejes: {coche.eje}\n Capacidad de carga: {coche.capacidadCarga}")


def main():
    opcion=True
    while opcion:
        os.system("cls")
        opcion=input("\n\t\t ::: Menu Principal ::.\n\t1.- Autos\n\t2.-Camionetas\n\t3.-Camiones\n\t4.-Salir\n\tElige un opción: ").lower().strip()
        match opcion:
            case "1":
                autos()
                input("Oprima tecla para continuar")
            case "2":
                camionetas()
                input("Oprima tecla para continuar")  
            case "3":
                camiones()
                input("Oprima tecla para continuar")
            case "4":
                input("Salir del Sistema")
                opcion=False   
            case _:
                input("Opcion invalidad ... vuelva a intertarlo ... ")      


if __name__=="__main__":
    main()
