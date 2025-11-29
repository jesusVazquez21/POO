'''
from tkinter import *

def cambiar_texto():
    mensajeCambiante.config(text="Texto cambiado")

def restaurar_texto():
    mensajeCambiante.config(text="Texto Original")

ventana = Tk()
ventana.geometry("800x600")
ventana.title("Uso de botones")
frame_principal = Frame(ventana)
frame_principal.config(
    bg="silver",
    width=800,
    height=100,
    border=2,
    relief=GROOVE
)
frame_principal.pack_propagate(False)
frame_principal.pack(pady=10)
label_titulo = Label(frame_principal,text="Uso de botones")
label_titulo.config(
    bg="silver",
    width=20
)
label_titulo.pack(pady=40)

mensajeCambiante=Label(ventana,text="Texto Original")
mensajeCambiante.pack()

boton_cambiar=Button(ventana,text="Cambiar texto", command=cambiar_texto)
boton_cambiar.pack()

boton_restaurar=Button(ventana,text="Restaurar texto", command=restaurar_texto)
boton_restaurar.pack(pady=15)

ventana.mainloop()

'''


from tkinter import *

ventana = Tk()
ventana.resizable(False, False)



def limpiar_ventana():
    for widget in ventana.winfo_children():
        widget.destroy()


def mostrar_vista_principal():
    limpiar_ventana()
    ventana.title("Aplicación - Vista Principal")
    ventana.geometry("600x400")
    
    
    inicioSesionExito=Label(ventana, text="Sesión Iniciada con Éxito", font=("Arial", 18, "bold"), fg="#2ecc71")
    inicioSesionExito.pack(pady=50)
    
    cerrarSesion=Button(
        ventana, 
        text="Cerrar Sesión", 
        command=mostrar_vista_login, 
        bg="#e74c3c", 
        fg="white", 
        font=("Arial", 12),
        width=15
    )
    cerrarSesion.pack(pady=30)


def mostrar_vista_login():
    limpiar_ventana()
    ventana.title("Inicio de Sesión Simple")
    ventana.geometry("500x350") 
    
    inicioSesion=Label(ventana, text="INICIAR SESIÓN", bg="#3498db", fg="white", font=("Arial", 14, "bold"), width=400)
    inicioSesion.pack(pady=0, ipady=15)
    
    usuario=Label(ventana, text="Usuario:" )
    usuario.pack(pady=0, ipady=15)
    
    
    contrasena=Label(ventana, text="Contraseña: ")
    contrasena.pack(pady=0, ipady=15)
    
    botonApp=Label(ventana, text="Presiona el botón para entrar a la aplicación.", font=("Arial", 10))
    botonApp.pack(pady=30)
    
    botonSesion=Button(
        ventana, 
        text="Iniciar Sesión", 
        command=mostrar_vista_principal, 
        bg="#2ecc71", 
        fg="white", 
        font=("Arial", 12),
        width=15
    )
    botonSesion.pack(pady=10)


mostrar_vista_login()

ventana.mainloop()

'''
from tkinter import *

# 1. INICIALIZACIÓN DE LA VENTANA
# Se crea la única ventana. Todas las funciones definidas después podrán acceder a ella.
ventana = Tk()
ventana.resizable(False, False)


# --- Funciones de la Aplicación ---

def limpiar_ventana():
    """Destruye todos los widgets en la ventana principal de forma concisa."""
    # Accede a 'ventana' que fue creada fuera de la función.
    [widget.destroy() for widget in ventana.winfo_children()]


def mostrar_vista_principal():
    """Muestra el contenido de la Vista Principal."""
    limpiar_ventana()
    ventana.title("Aplicación - Vista Principal")
    ventana.geometry("600x400")
    
    # --- Contenido de la Vista Principal ---
    
    Label(ventana, text="Sesión Iniciada con Éxito", font=("Arial", 18, "bold"), fg="#2ecc71").pack(pady=50)
    
    Button(
        ventana, 
        text="Cerrar Sesión", 
        command=mostrar_vista_login, 
        bg="#e74c3c", 
        fg="white", 
        font=("Arial", 12),
        width=15
    ).pack(pady=30)


def mostrar_vista_login():
    """Muestra el contenido de la pantalla de 'Inicio de Sesión'."""
    limpiar_ventana()
    ventana.title("Inicio de Sesión Simple")
    ventana.geometry("400x250") 

    # --- Contenido de la Vista Login ---
    
    Label(ventana, text="INICIAR SESIÓN", bg="#3498db", fg="white", font=("Arial", 14, "bold"), width=400).pack(pady=0, ipady=15)
    
    Label(ventana, text="Presiona el botón para entrar a la aplicación.", font=("Arial", 10)).pack(pady=30)
    
    Button(
        ventana, 
        text="Iniciar Sesión", 
        command=mostrar_vista_principal, 
        bg="#2ecc71", 
        fg="white", 
        font=("Arial", 12),
        width=15
    ).pack(pady=10)


# --- 2. PUNTO DE EJECUCIÓN ---

# Llama a la primera vista (Login)
mostrar_vista_login()

# Inicia el bucle principal de tkinter (mainloop)
ventana.mainloop()
'''