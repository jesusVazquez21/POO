from view.interfaz import Vista
from tkinter import *

class App:
    @staticmethod
    def main(ventana):
        view = Vista(ventana)

if __name__ == "__main__":
    ventana = Tk()
    App.main(ventana)
    ventana.mainloop()