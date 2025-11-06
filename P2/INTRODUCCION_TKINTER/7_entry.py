from tkinter import *

def entrar():
    lbl_resultado.config(
    text=f"Bienvenido al sistema {nombre.get()}",
    bg="#687d8b", 
    fg="white", 
    font=("Arial", 14, "italic"), 
    width=400, 
    height=5, 
    border=2,
    relief=GROOVE
)

def borrar():
    # color_ventana=ventana.cget("bg")
    # lbl_resultado.config(
    #     text="", 
    #     bg=color_ventana,
    #     border=0
    # )
    
    
    txt_nombre.delete(0, END)
    txt_password.delete(0, END)
    txt_nombre.focus()
    lbl_resultado.destroy()
    
def salir():
    ventana.quit()
    

ventana = Tk()
ventana.title("Uso de ENTRY")
ventana.geometry("800x500") 
ventana.resizable(False, False)


bienvenida=Label(ventana, text="Acceso al Sistema")
bienvenida.config(
    bg="#89c1e7", 
    fg="darkblue", 
    font=("Arial", 14, "italic"), 
    width=400, 
    height=5, 
    relief=GROOVE
)
bienvenida.pack(pady=10)

marco_principal=Frame(ventana, width=800, height=300)
marco_principal.pack()

lbl_nombre=Label(marco_principal, text="Ingrese el nombre: ")
lbl_nombre.grid(row=0, column=0, pady=5, padx=5, )

nombre=StringVar()
txt_nombre=Entry(marco_principal, textvariable=nombre)
txt_nombre.focus()
txt_nombre.grid(row=0, column=1, pady=5, padx=5)

lbl_password=Label(marco_principal, text="Ingrese la contraseña:  ")
lbl_password.grid(row=1, column=0, pady=5, padx=5)

txt_password=Entry(marco_principal, show="*")
txt_password.grid(row=1, column=1, pady=5, padx=5)

#------MARCO DE BOTONES------
marco_botones=Frame(ventana, width=800, height=100)
marco_botones.pack()


btn_entrar=Button(
        marco_botones, 
        text="Entrar", 
        bg="#818181", 
        fg="white",
        activeforeground="darkgreen",
        command=entrar,
    )
btn_entrar.grid(row=3, column=0, pady=15, padx=5)

btn_borrar=Button(marco_botones, text="Borrar", command="borrar")
btn_borrar.config(
        bg="#818181", 
        fg="white",
        activeforeground="red",
        command=borrar,
    )
btn_borrar.grid(row=3, column=1, pady=5, padx=5)

btn_salir=Button(marco_botones, text="Salir", command=salir)
btn_salir.grid(row=3, column=2, pady=5, padx=5)

lbl_resultado=Label(ventana, text="")
lbl_resultado.pack(pady=5)

ventana.mainloop()