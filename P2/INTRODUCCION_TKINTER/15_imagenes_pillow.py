#Es necesario instalar la siguiente libreria: 
# pip install --upgrade pillow
# pip install --upgrade pip

from tkinter import *
import os

ventana = Tk()
ventana.title("Imagenes con Pillow")
ventana.geometry("500x500")

def mensaje(tipo):
    resultado.config(text=f"{tipo}")

# Obtener la ruta absoluta del directorio donde está este archivo .py
ruta_base = os.path.dirname(os.path.abspath(__file__))
print(ruta_base)

# Construir la ruta completa al archivo de imagen
ruta_imagen = os.path.join(ruta_base, "image/logo_utd.png")
print(ruta_imagen)

#1er de agregar imagenes con la libreria de Tkinter ya incluidas
#PhotoImage solo permite archivos con extension .png, .gif y .pgm / .ppm

imagen=PhotoImage(file=ruta_imagen)
#incluir o mostrar la imgagen dentro de un Label y Button
etiqueta=Label(ventana,image=imagen,text="Somos Bufalos ... UTD",compound="top")
etiqueta.pack()

boton=Button(ventana,image=imagen,command=lambda: mensaje("Hola Python"))
boton.pack()

resultado=Label(ventana,text="")
resultado.pack()

ventana.mainloop()