from tkinter import *

def hazclick():
    bienvenida.config(
    text="POO con python",
    bg="#8af774", 
    fg="red", 
    font=("Arial", 14, "italic"), 
    width=400, 
    height=5, 
    border=2,
    relief=GROOVE
)

def regresarClick():
    bienvenida.config(
    text="Bienvenido a Tkinter",
    bg="#89c1e7", 
    fg="darkblue", 
    font=("Arial", 14, "italic"), 
    width=400, 
    height=5, 
    border=2,
    relief=GROOVE
)

ventana = Tk()
ventana.title("Personalizacion de Widgets U Objetos")
ventana.geometry("500x500") 
ventana.resizable(False, False)

bienvenida=Label(ventana, text="Bienvenidos a Tkinter")
bienvenida.config(
    bg="#89c1e7", 
    fg="darkblue", 
    font=("Arial", 14, "italic"), 
    width=400, 
    height=5, 
    relief=GROOVE
)
bienvenida.pack(pady=0, ipady=15)


botonColor=Button(
        ventana, 
        text="Haz click aqui", 
        bg="#818181", 
        fg="white",
        activeforeground="darkgreen",
        command=hazclick,
        font=("Arial", 20, "bold" ),
        width=15
    )
botonColor.pack(pady=10)

botonRegresar=Button(ventana, text="Haz click aqui", command=regresarClick)
botonRegresar.config(
        bg="#818181", 
        fg="black",
        activeforeground="red",
        font=("Arial", 20, "bold" ),
        width=15
    )
botonRegresar.pack(pady=10)

ventana.mainloop()