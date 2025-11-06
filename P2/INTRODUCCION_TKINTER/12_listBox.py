from tkinter import *

def mostrar():
    valor=lstbx.get(lstbx.curselection())
    
    resultado.config(text=f"Seleccionaste: {valor}")

ventana = Tk()
ventana.title("ListBox")
ventana.geometry("500x500") 
ventana.resizable(False, False)


lstbx=Listbox(ventana, selectmode=SINGLE)
lstbx.pack()

opciones=["azul", "rojo", "verde", "amarillo"]
for i in opciones:
    lstbx.insert(END, i)


btn=Button(ventana, text="Mostrar seleccion del Usuario", command=mostrar)
btn.pack()

resultado=Label(ventana, text="")
resultado.pack()














ventana.mainloop()