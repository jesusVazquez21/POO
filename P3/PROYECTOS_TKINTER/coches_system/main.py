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
    Nombre del Commit  "commit_01-12-25"

"""

'''
2 Diciembre
    1) INTERFACES
        1.1 Insertar_camionetas()
        1.2 consultar_camionetas()
        1.3 cambiar_camionetas()
        1.4 borrar_camionetas()
        2.1 insertar_camiones()
        2.2 consultar_camiones()
        2.3 cambiar_camiones()
        2.4 borrar_camiones()
        
    Productos Entregbles:
    Interaccion con todas las interfaces
    Nombre del commit "commit_02_12_25"
'''
'''
3 Diciembre
    1)CONTROLADOR
        1.1 menu_principal()
        1.2 menu_acciones()
        1.3 insertar_autos()
        1.4 consultar_autos()
        1.5 cambiar_autos()
        1.6 borrar_autos()
    Productos Ebtregables:
    Interaccion con la fucionalidad (controlador) de las interfaces anteriores
    Nombre del Commit "commit_03_12_25"
'''
'''
4 Diciembre
    1)Controlador:
        1.1 insertar_camionetas()
        1.2 consultar_camionetas()
        1.3 cambiar_camionetas()
        1.4 borrar_camionetas()
    
    Productos Entregables:
    Interaccion con la funcionalidad (controlador) de las interfaces anteriores
    Nombre del Commit "commit_04_12_25"
'''
'''
5 Diciembre
    1)Controlador:
        1.1 insertar_camiones()
        1.2 consultar_camiones()
        1.3 cambiar_camiones()
        1.4 borrar_camiones()
        
    Productos Entregables:
    Interaccion con la funcionalidad (controlador) de las interfaces anteriores
    Nombre del Commit "commit_05_12_25"
'''
class App:
    @staticmethod
    def main(ventana):
        view = Vista(ventana)

if __name__ == "__main__":
    ventana = Tk()
    App.main(ventana)
    ventana.mainloop()