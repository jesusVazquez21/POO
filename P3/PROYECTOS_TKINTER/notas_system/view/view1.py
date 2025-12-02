from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from controller.controlador1 import Controlador

id_user = None
nom_user = ""
ape_user = ""
class View:
    def __init__(self, ventana):
        self.ventana=ventana    
        ventana.title("GEstión de Notas")
        ventana.geometry("700x600")
        ventana.resizable(False,False)
        ventana.config(bg="#ffffff")
        self.interfazPrincipal(ventana)
    
    @staticmethod
    def limpiar_ventana(ventana):
        for widget in ventana.winfo_children():
            # widget.destroy()
            widget.pack_forget()
    
    @staticmethod
    def interfazPrincipal(ventana):
        View.limpiar_ventana(ventana)
        lbl_titulo=Label(ventana, text="..:: Menú Principal::..", bg="#ffffff")
        lbl_titulo.pack()

        btn_registro = Button(ventana, text="1.- Registro", justify=CENTER, command=lambda: View.menuRegistro(ventana))
        btn_registro.pack(pady=10)

        btn_login = Button(ventana, text="2.- Login", justify=CENTER, command= lambda:View.menuIniciarSesion(ventana))
        btn_login.pack(pady=10)
        
        btn_salir = Button(ventana, text="3.- Salir", command=ventana.quit, justify=CENTER)
        btn_salir.pack(pady=10)
        
    @staticmethod
    def procesarRegistro(ventana, nombre, apellido, email, password):
        exito = Controlador.registro(nombre, apellido, email, password)
        if exito:
            View.menuIniciarSesion(ventana)

    @staticmethod
    def menuRegistro(ventana):
        View.limpiar_ventana(ventana)
        lbl_titulo=Label(ventana, text="..:: Ventana de Registro::..", bg="#ffffff")
        lbl_titulo.pack()

        var_nombre =StringVar()
        var_apellido =StringVar()
        var_email = StringVar()
        var_pass =StringVar()

        lbl_nombre = Label(ventana, text="¿Cual es tu nombre?", bg="#f0f0f0")
        lbl_nombre.pack()
        entry_nombre = Entry(ventana, textvariable=var_nombre, width=30)
        entry_nombre.pack()

        lbl_apellido = Label(ventana, text="¿Cuales son tus apellidos?", bg="#f0f0f0")
        lbl_apellido.pack()
        entry_apellido = Entry(ventana, textvariable=var_apellido, width=30)
        entry_apellido.pack()

        lbl_email = Label(ventana, text="Ingresa tu email", bg="#f0f0f0")
        lbl_email.pack()
        entry_email = Entry(ventana, textvariable=var_email, width=30)
        entry_email.pack()

        lbl_pass = Label(ventana, text="Ingresa tu Contraseña:", bg="#f0f0f0")
        lbl_pass.pack()
        entry_pass = Entry(ventana, textvariable=var_pass, show="*", width=30)
        entry_pass.pack()
        
        btn_registrar = Button(
            ventana, text="Registrar", font=("Arial", 10), 
            command=lambda: View.procesarRegistro(ventana, var_nombre.get(), var_apellido.get(), var_email.get(), var_pass.get())
        )
        btn_registrar.pack(pady=20) 

        btn_volver = Button(
            ventana, 
            text="Volver", 
            command=lambda: View.interfazPrincipal(ventana)
        )
        btn_volver.pack(pady=5)
    
    @staticmethod
    def procesarLogin(ventana, email, password):
        usuario = Controlador.iniciarsesion(email, password)
        if usuario:
            View.menuNotas(ventana, usuario[0], usuario[1], usuario[2])
    
    @staticmethod
    def menuIniciarSesion(ventana):
        View.limpiar_ventana(ventana)
        lbl_titulo=Label(ventana, text="..:: Ventana de Inicio de Sesion::..", bg="#ffffff")
        lbl_titulo.pack()
        
        var_email = StringVar()
        var_pass = StringVar()

        lbl_email = Label(ventana, text="Ingresa tu Email", bg="#f0f0f0")
        lbl_email.pack()
        entry_email = Entry(ventana, textvariable=var_email, width=30)
        entry_email.pack()

        lbl_pass = Label(ventana, text="Ingresa tu Contraseña", bg="#f0f0f0")
        lbl_pass.pack()
        entry_pass = Entry(ventana, textvariable=var_pass, show="*", width=30)
        entry_pass.pack()
        
        btn_entrar = Button(
            ventana, 
            text="Entrar", 
            width=15, 
            font=("Arial", 10),
            command=lambda: View.procesarLogin(ventana, var_email.get(), var_pass.get())
                ) 
        btn_entrar.pack(pady=(30, 10)) 

        btn_volver = Button(
            ventana, 
            text="Volver", 
            width=15,
            font=("Arial", 10),
            command=lambda: View.interfazPrincipal(ventana)
        )
        btn_volver.pack(pady=5)

    @staticmethod
    def menuNotas(ventana, usuario_id, nombre, apellidos):
        View.limpiar_ventana(ventana)
        global id_user, nom_user, ape_user
        
        id_user=usuario_id
        nom_user=nombre
        ape_user=apellidos

        lbl_titulo=Label(ventana, text=f"Bienvenido {nom_user} {ape_user}", bg="#ffffff")
        lbl_titulo.pack()
        
        btn_crear = Button(
            ventana, text="1.- Crear", width=20,
            command=lambda: View.crearNota(ventana))
        btn_crear.pack(pady=5)

        btn_mostrar = Button(
            ventana, text="2.- Mostrar", width=20,
            command=lambda: View.mostrarNota(ventana))
        btn_mostrar.pack(pady=5)

        btn_cambiar = Button(
            ventana, text="3.- Cambiar", width=20,
            command=lambda: View.cambiarNota(ventana))
        btn_cambiar.pack(pady=5)

        btn_eliminar = Button(
            ventana, text="4.- Eliminar", width=20,
            command=lambda: View.menuEliminarNota(ventana))
        btn_eliminar.pack(pady=5)

        btn_regresar = Button(
            ventana, text="5.- Regresar", width=20,
            command=lambda: View.interfazPrincipal(ventana)
        )
        btn_regresar.pack(pady=20)

    @staticmethod
    def crearNota(ventana):
        View.limpiar_ventana(ventana)
        lbl_titulo = Label(ventana, text="..:: Crear Nota ::..", bg="#ffffff", font=("Arial", 12, "bold"))
        lbl_titulo.pack(pady=5)
        lbl_tittle=Label(ventana, text=f"Bienvenido {nom_user} {ape_user}", bg="#ffffff")
        lbl_tittle.pack()
        
        lbl_titu = Label(ventana, text="Titulo de la nota: ",  bg="#ffffff")
        lbl_titu.pack()
        entry_titulo = Entry(ventana, width=30)
        entry_titulo.focus()
        entry_titulo.pack()
        
        lbl_descri=Label(ventana, text="Descripcion", bg="#ffffff")
        lbl_descri.pack()
        entry_descri = Entry(ventana, width=30)
        entry_descri.pack()
        
        btn_guardar = Button(
            ventana, text="Guardar Nota", width=20,
            command=lambda: Controlador.crearNota(id_user, entry_titulo.get(), entry_descri.get())
        )
        btn_guardar.pack(pady=5)

        btn_regresar = Button(
            ventana, text="Regresar", width=20,
            command=lambda: View.menuNotas(ventana, id_user, nom_user, ape_user)
        )   
        btn_regresar.pack(pady=20)

    @staticmethod
    def mostrarNota(ventana):
        View.limpiar_ventana(ventana) 
        
        lbl_titulo = Label(ventana, text="..:: Mis Notas ::..", bg="#ffffff", font=("Arial", 12, "bold"))
        lbl_titulo.pack(pady=5)
        
        lbl_user = Label(ventana, text=f"Usuario: {nom_user} {ape_user}", bg="#ffffff")
        lbl_user.pack()

        registros = Controlador.obtenerNotas(id_user)
        
        texto_notas = ""
        
        if registros:
            for fila in registros:
                texto_notas += f"ID: {fila[0]} | Título: {fila[2]} | Fecha: {fila[4]}\n" \
                            f"Descripción: {fila[3]}\n" \
                            f"----------------------------------------------------\n"
        else:
            texto_notas = "\nNo tienes notas guardadas todavía."

        lbl_registros = Label(ventana, text=texto_notas, bg="#ffffff", justify=LEFT) 
        lbl_registros.pack(pady=10)
        
        btn_regresar = Button(
            ventana, 
            text="Volver", 
            width=20,
            command=lambda: View.menuNotas(ventana, id_user, nom_user, ape_user) 
        )
        btn_regresar.pack(pady=20)

    @staticmethod
    def cambiarNota(ventana):
        View.limpiar_ventana(ventana)
        
        lbl_titulo = Label(ventana, text="..:: Modificar Nota ::..", font=("Arial", 12, "bold"), bg="#ffffff")
        lbl_titulo.pack(pady=20)
        
        lbl_user = Label(ventana, text=f"Usuario: {nom_user}", bg="#ffffff")
        lbl_user.pack()

        lbl_id = Label(ventana, text="ID de la Nota a cambiar:", bg="#f0f0f0")
        lbl_id.pack(pady=(10, 5))
        entry_id = Entry(ventana, width=30)
        entry_id.pack()

        lbl_nuevo_titulo = Label(ventana, text="Nuevo Titulo:", bg="#f0f0f0")
        lbl_nuevo_titulo.pack(pady=(10, 5))
        entry_titulo = Entry(ventana, width=30)
        entry_titulo.pack()

        lbl_nueva_desc = Label(ventana, text="Nueva Descripción:", bg="#f0f0f0")
        lbl_nueva_desc.pack(pady=(10, 5))
        entry_desc = Entry(ventana, width=30)
        entry_desc.pack()

        btn_guardar = Button(
            ventana, 
            text="Guardar Cambios", 
            width=20, 
            command=lambda: Controlador.actualizarNota(entry_id.get(), entry_titulo.get(), entry_desc.get()
            )
        )
        btn_guardar.pack(pady=(30, 10))

        btn_volver = Button(
            ventana, 
            text="Volver", 
            width=15, 
            command=lambda: View.menuNotas(ventana, id_user, nom_user, ape_user)
        )
        btn_volver.pack(pady=5)

    @staticmethod
    def menuEliminarNota(ventana):
        View.limpiar_ventana(ventana)
        
        lbl_titulo = Label(ventana, text="..:: Eliminar Nota ::..", font=("Arial", 12, "bold"), bg="#ffffff", fg="red")
        lbl_titulo.pack(pady=20)

        lbl_user = Label(ventana, text=f"Usuario: {nom_user}", bg="#ffffff")
        lbl_user.pack()

        lbl_id = Label(ventana, text="Introduce el ID de la Nota a eliminar:", bg="#f0f0f0")
        lbl_id.pack(pady=(20, 5))
        
        entry_id_eliminar = Entry(ventana, width=30)
        entry_id_eliminar.pack(pady=5)
        
        btn_eliminar = Button(
            ventana, 
            text="ELIMINAR DEFINITIVAMENTE", 
            width=25, 
            command=lambda: Controlador.eliminarNota(entry_id_eliminar.get())
        )
        btn_eliminar.pack(pady=(30, 10))

        btn_volver = Button(
            ventana, 
            text="Volver", 
            width=15, 
            command=lambda: View.menuNotas(ventana, id_user, nom_user, ape_user)
        )
        btn_volver.pack(pady=5)
        
        