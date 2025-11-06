from tkinter import *

def mostrarComentario():
    mostrarContenido=comentario.get("1.0", END).strip()
    resultado.config(text=f"Comentario:\n{mostrarContenido}")

ventana = Tk()
ventana.title("Text")
ventana.geometry("800x500") 
ventana.resizable(False, False)

bienvenida=Label(ventana, text="Escriba su comentario")
bienvenida.config( 
    fg="darkblue", 
    font=("Arial", 14, "italic")
)

bienvenida.pack(pady=10)


comentario=Text(ventana, width=40, height=5)
comentario.pack()

boton= Button(ventana, text="Mostrar comentario", command=mostrarComentario)
boton.pack()

resultado=Label(ventana, text="")
resultado.pack()




ventana.mainloop()