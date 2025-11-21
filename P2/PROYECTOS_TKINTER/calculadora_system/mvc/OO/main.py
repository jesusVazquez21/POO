'''
Crear una calculadora: 
1.- Dos campos de texto
2.- 4 Botones para las Operaciones
3.- Mostrar el resultado
4.- Programacion de forma Orientada a Objetos
5.-Considerar MVC
'''
from view import interfaz
from tkinter import *
class App:
    @staticmethod
    def main(ventana):
        view=interfaz.Vista(ventana)
        
if __name__ == "__main__":
    ventana=Tk()
    App.main(ventana)
    ventana.mainloop()
    
    
    
    
    
    
    
    
# class App:
#     def __init__(self, ventana):
#         view=interfaz.Vista(ventana)
    
# if __name__ == "__main__":
#     ventana=Tk()
#     app=App(ventana)
#     ventana.mainloop()
    
    
    
    
    
    
    
    