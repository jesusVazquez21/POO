from tkinter import *

def mostrar():
    resultado.config(text=f"{valor.get()}")

ventana = Tk()
ventana.title("Scale")
ventana.geometry("500x500") 
ventana.resizable(False, False)



valor=IntVar()
scle=Scale(ventana, variable=valor, orient="horizontal", from_=0, to=150)
scle.pack()

btn=Button(ventana, text="Mostrar valor", command=mostrar)
btn.pack()

muestra=Label(ventana, text="Valor seleccionado por el usuario:")
muestra.pack()

resultado=Label(ventana, text="")
resultado.pack()









ventana.mainloop()