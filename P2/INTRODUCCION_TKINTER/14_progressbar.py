from tkinter import *
from tkinter import ttk


def progreso():
  barraprogreso['value']=0
  ventana.update()
  for i in range(101):
    barraprogreso["value"]=i
    ventana.update()
    ventana.after(50)

ventana = Tk()
ventana.title("Progressbar")
ventana.geometry("500x500")

barraprogreso=ttk.Progressbar(ventana,mode="determinate",length=200)
barraprogreso.pack()

barraprogreso['value']=0
ventana.update()
for i in range(101):
    barraprogreso["value"]=i
    ventana.update()
    ventana.after(50)

boton = Button(ventana , text="Iniciar progreso" , command=progreso)
boton.pack()



ventana.mainloop()