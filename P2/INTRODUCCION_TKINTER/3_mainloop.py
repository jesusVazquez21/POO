from tkinter import *

ventana=Tk()
ventana.title("MainLoop")
ventana.geometry("800x600")

marco=Frame(ventana)
marco.config(
    bg="#A40000",
    bd=5,
    height=400,
    width=600,
    relief=RAISED
)

marco.pack(
    side=LEFT, 
    anchor=CENTER
)


ventana.mainloop()
