"""
1.- Implementar MVC
2.-Paradigma POO
3.-App de Escritoio con interfaz gráfica
"""

from tkinter import *
from view import view1

class App:
    @staticmethod
    def main(ventana):
        view=view1.View(ventana)
        
if __name__ == "__main__":
    ventana=Tk()
    App.main(ventana)
    ventana.mainloop()