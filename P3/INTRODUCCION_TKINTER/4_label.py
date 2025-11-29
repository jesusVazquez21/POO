from tkinter import *

ventana=Tk()
ventana.title("Etiquetas")
ventana.geometry("800x600")

#Etiquetas o Label

etiqueta1=Label(ventana, text="Nombre de la persona").pack()
marco1=Frame(ventana, bg="#157E24", width=300, height=200)
marco1.pack_propagate(False)
marco1.pack()


etiqueta2=Label(marco1, text="Soy una etiqueta dentro de un marco", bg="#157E24").pack()
ventana.mainloop()