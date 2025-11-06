from tkinter import *

def mostrarSeleccion():
    resultado.config(text=f"Opcion seleccionada: {opcion.get()}")

ventana = Tk()
ventana.title("RadioButton")
ventana.geometry("500x500") 
ventana.resizable(False, False)

opcion=StringVar()
rbtn1=Radiobutton(ventana, text="Opcion 1", variable=opcion, value="opcion 1")
rbtn1.pack()


rbtn2=Radiobutton(ventana, text="Opcion 2", variable=opcion, value="opcion 2")
rbtn2.pack()


rbtn3=Radiobutton(ventana, text="Opcion 3", variable=opcion, value="opcion 3")
rbtn3.pack()


btn_mostrar=Button(ventana, text="Mostrar Seleccion", command=mostrarSeleccion)
btn_mostrar.pack()

resultado=Label(ventana, text="")
resultado.pack()

ventana.mainloop()