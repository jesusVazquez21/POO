"""
Tkinger trabaja a traves de interfaces, es una vilviteca de Python que  permite crear aplicaciones en Python para escritorio
"""

import tkinter as tk

ventana=tk.Tk()

ventana.title("Mi primer App Grafica en Tkinter con Python")
ventana.geometry("900x600")
ventana.resizable(False, False)
ventana.mainloop() #Metodo que permite tener la ventana abierta e intercactuar con ella