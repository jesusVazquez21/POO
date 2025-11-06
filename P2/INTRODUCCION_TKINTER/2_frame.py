from tkinter import *

ventana=Tk()
ventana.title("Uso de Frame o Marcos")
ventana.geometry("800x600")

#Marcos o Frame
marco=Frame(ventana, width=300, height=200, bg="silver", borderwidth=2, relief=SOLID)
marco.pack_propagate(False)
marco.pack(pady=100)

marco2=Frame(marco, width=200, height=100, bg="lightBlue", borderwidth=2, relief=GROOVE).pack(padx=100, pady=50)
ventana.mainloop()