from view.interfaz import Vista
from tkinter import *


"""
1Er Diciembre
    1) Implementacion de MVC
    2) POO
    3) Interfaces
    3.1 menu_principal()
    3.2 menu_acciones()
    3.3 insertar_autos()

PRODUCTOS ENTREGABLES
    Estructura del proyecto basada en MVC
    Modulo Principal Main
    Interaccion con las interfaces
"""
class App:
    @staticmethod
    def main(ventana):
        view = Vista(ventana)

if __name__ == "__main__":
    ventana = Tk()
    App.main(ventana)
    ventana.mainloop()