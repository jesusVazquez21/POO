from tkinter import *

def mensaje(tipo):
    resultado.config(Text=f"{tipo}")
    
def borrar():
    ventana.quit()

ventana = Tk()
ventana.title("Menu")
ventana.geometry("500x500") 
ventana.resizable(False, False)


menuBar=Menu(ventana)
ventana.config(menu=menuBar)

archivoMenu= Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Archivo", menu=archivoMenu)
archivoMenu.add_command(label="Nuevo Archivo", command=lambda: mensaje("Nuevo Archivo"))
archivoMenu.add_command(label="Guardar Archivo", command=lambda: mensaje("Guardar Archivo"))
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command=borrar)

archivoEditar= Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Edicion", menu=archivoEditar)
archivoEditar.add_command(label="Copiar", command=lambda: mensaje("Copiar"))
archivoEditar.add_command(label="Recortar", command=lambda: mensaje("Recortar"))
archivoEditar.add_separator()
archivoEditar.add_command(label="Salir", command=borrar)



resultado=Label(ventana, text="")
resultado.pack()







ventana.mainloop()