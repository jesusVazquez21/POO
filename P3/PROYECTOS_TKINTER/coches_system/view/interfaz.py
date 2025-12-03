from tkinter import *
from tkinter import ttk
from model import coches
from controller.funciones import Controlador
from tkinter import messagebox

class Vista:
    def __init__(self, window):
        self.wind = window
        self.wind.title("Sistema de Gestión de Vehículos")
        self.wind.geometry("1100x700")
        self.wind.resizable(False, False)
        
        self.init_variables()
        
        self.menu_principal()

    def init_variables(self):
        # Variables Autos
        self.a_id = StringVar() 
        self.a_marca = StringVar()
        self.a_color = StringVar()
        self.a_modelo = StringVar() 
        self.a_vel = IntVar()
        self.a_hp = IntVar()
        self.a_plazas = IntVar()
        # Variables Camionetas
        self.c_id = StringVar()
        self.c_marca = StringVar()
        self.c_color = StringVar()
        self.c_modelo = StringVar()
        self.c_vel = IntVar()
        self.c_hp = IntVar()
        self.c_plazas = IntVar()
        self.c_traccion = StringVar()
        self.c_cerrada = StringVar()
        # Variables Camiones
        self.t_id = StringVar()
        self.t_marca = StringVar()
        self.t_color = StringVar()
        self.t_modelo = StringVar()
        self.t_vel = IntVar()
        self.t_hp = IntVar()
        self.t_plazas = IntVar()
        self.t_ejes = IntVar()
        self.t_carga = IntVar()

    def limpiar_ventana(self):
        for widget in self.wind.winfo_children():
            widget.destroy()

    def menu_principal(self):
        self.limpiar_ventana()
        Label(self.wind, text="MENU PRINCIPAL").pack(pady=20)
        
        Button(self.wind, text="1. Autos", command=self.menu_autos, width=30).pack(pady=5)
        Button(self.wind, text="2. Camionetas", command=self.menu_camionetas, width=30).pack(pady=5)
        Button(self.wind, text="3. Camiones", command=self.menu_camiones, width=30).pack(pady=5)
        Button(self.wind, text="4. Salir", command=self.wind.quit, width=30).pack(pady=20)

    def crear_menu_crud(self, titulo, cmd_ins, cmd_con, cmd_act, cmd_eli):
        self.limpiar_ventana()
        Label(self.wind, text=f"MENU {titulo.upper()}").pack(pady=20)
        
        Button(self.wind, text="1.- Insertar", command=cmd_ins, width=30).pack(pady=5)
        Button(self.wind, text="2.- Consultar", command=cmd_con, width=30).pack(pady=5)
        Button(self.wind, text="3.- Actualizar", command=cmd_act, width=30).pack(pady=5)
        Button(self.wind, text="4.- Eliminar", command=cmd_eli, width=30).pack(pady=5)
        Button(self.wind, text="5.- Regresar", command=self.menu_principal, width=30).pack(pady=20)

    def menu_autos(self):
        self.crear_menu_crud("Autos", self.vista_auto_insertar, self.vista_auto_consultar, self.vista_auto_actualizar, self.vista_auto_eliminar)

    def menu_camionetas(self):
        self.crear_menu_crud("Camionetas", self.vista_camioneta_insertar, self.vista_camioneta_consultar, self.vista_camioneta_actualizar, self.vista_camioneta_eliminar)

    def menu_camiones(self):
        self.crear_menu_crud("Camiones", self.vista_camion_insertar, self.vista_camion_consultar, self.vista_camion_actualizar, self.vista_camion_eliminar)

    def vista_auto_insertar(self):
        self.limpiar_ventana()
        self.limpiar_campos_auto()
        Label(self.wind, text="INSERTAR AUTO").pack(pady=10)
        self.entry_form_autos()
        Button(self.wind, text="Guardar", command=self.guardar_auto).pack(pady=10)
        Button(self.wind, text="Regresar", command=self.menu_autos).pack(pady=5)

    def vista_auto_consultar(self):
        self.limpiar_ventana()
        Label(self.wind, text="CONSULTA DE AUTOS").pack(pady=10)
        
        lista = Listbox(self.wind, width=100, height=20)
        lista.pack(pady=10)
        
        registros = coches.Autos.consultar()
        for fila in registros:
            lista.insert(END, f"ID:{fila[0]} | Marca: {fila[1]} | Color: {fila[2]} | Modelo{fila[3]} | Velocidad:{fila[4]} | Caballaje:{fila[5]} | Plazas:{fila[6]}")
            
        Button(self.wind, text="Regresar", command=self.menu_autos).pack(pady=10)

    def vista_auto_actualizar(self):
        self.limpiar_ventana()
        self.limpiar_campos_auto()
        Label(self.wind, text="ACTUALIZAR AUTO").pack(pady=10)
        
        frame_buscar = Frame(self.wind)
        frame_buscar.pack(pady=5)
        Label(frame_buscar, text="ID a Buscar:").pack(side=LEFT)
        Entry(frame_buscar, textvariable=self.a_id, width=10).pack(side=LEFT, padx=5)
        Button(frame_buscar, text="Buscar ID", command=self.buscar_auto).pack(side=LEFT)
        
        Label(self.wind, text="-- Editar Datos --").pack(pady=5)
        self.entry_form_autos()
        
        Button(self.wind, text="Actualizar Cambios", command=self.editar_auto).pack(pady=10)
        Button(self.wind, text="Regresar", command=self.menu_autos).pack(pady=5)

    def vista_auto_eliminar(self):
        self.limpiar_ventana()
        self.limpiar_campos_auto()
        Label(self.wind, text="ELIMINAR AUTO").pack(pady=10)
        
        Label(self.wind, text="ID a Eliminar:").pack()
        Entry(self.wind, textvariable=self.a_id).pack()
        
        Button(self.wind, text="Eliminar", command=self.eliminar_auto).pack(pady=10)
        Button(self.wind, text="Regresar", command=self.menu_autos).pack(pady=5)
        
    def buscar_auto(self):
        if not self.a_id.get():
            messagebox.showwarning("Alerta", "Escribe un ID primero")
            return
        
        dato = coches.Autos.buscar(self.a_id.get())
        if dato:
            self.a_marca.set(dato[1])
            self.a_color.set(dato[2])
            self.a_modelo.set(dato[3])
            self.a_vel.set(dato[4])
            self.a_hp.set(dato[5])
            self.a_plazas.set(dato[6])
        else:
            messagebox.showerror("Error", "No se encontró ningún auto con ese ID")
            self.limpiar_campos_auto()

    def entry_form_autos(self):
        Label(self.wind, text="Marca:").pack()
        Entry(self.wind, textvariable=self.a_marca).pack()

        Label(self.wind, text="Color:").pack()
        Entry(self.wind, textvariable=self.a_color).pack()

        Label(self.wind, text="Modelo:").pack()
        Entry(self.wind, textvariable=self.a_modelo).pack()

        Label(self.wind, text="Velocidad:").pack()
        Entry(self.wind, textvariable=self.a_vel).pack()

        Label(self.wind, text="Potencia:").pack()
        Entry(self.wind, textvariable=self.a_hp).pack()

        Label(self.wind, text="Plazas:").pack()
        Entry(self.wind, textvariable=self.a_plazas).pack()

    def guardar_auto(self):
        res = coches.Autos.insertar(self.a_marca.get(), self.a_color.get(), self.a_modelo.get(), self.a_vel.get(), self.a_hp.get(), self.a_plazas.get())
        Controlador.respuesta(res)
        if res: 
            self.limpiar_campos_auto()

    def editar_auto(self):
        res = coches.Autos.actualizar(self.a_id.get(), self.a_marca.get(), self.a_color.get(), self.a_modelo.get(), self.a_vel.get(), self.a_hp.get(), self.a_plazas.get())
        Controlador.respuesta(res)
        if res: 
            self.limpiar_campos_auto()

    def eliminar_auto(self):
        res=coches.Autos.eliminar(self.a_id.get())
        Controlador.respuesta(res)
        if res:
            self.limpiar_campos_auto()
    
    def limpiar_campos_auto(self):
        self.a_id.set(""); self.a_marca.set(""); self.a_color.set(""); self.a_modelo.set(""); self.a_vel.set(0); self.a_hp.set(0); self.a_plazas.set(0)

    #----------CAMIONETAS---------------
    
    def vista_camioneta_insertar(self):
        self.limpiar_ventana()
        self.limpiar_campos_camioneta()
        Label(self.wind, text="INSERTAR CAMIONETA").pack(pady=10)
        self.entry_form_camionetas()
        Button(self.wind, text="Guardar", command=self.guardar_camioneta).pack(pady=10)
        Button(self.wind, text="Regresar", command=self.menu_camionetas).pack(pady=5)

    def vista_camioneta_consultar(self):
        self.limpiar_ventana()
        Label(self.wind, text="CONSULTA DE CAMIONETAS").pack(pady=10)
        
        lista = Listbox(self.wind, width=100, height=20)
        lista.pack(pady=10)
        
        registros = coches.Camionetas.consultar()
        for fila in registros:
            lista.insert(END, f"ID:{fila[0]} | Marca: {fila[1]} | Color: {fila[2]} | Modelo{fila[3]} | Velocidad:{fila[4]} | Caballaje:{fila[5]} | Plazas:{fila[6]} | Traccion:{fila[7]} | Cerrada:{fila[8]}")
            
        Button(self.wind, text="Regresar", command=self.menu_camionetas).pack(pady=10)

    def vista_camioneta_actualizar(self):
        self.limpiar_ventana()
        self.limpiar_campos_camioneta()
        Label(self.wind, text="ACTUALIZAR CAMIONETA").pack(pady=10)
        
        frame_buscar = Frame(self.wind)
        frame_buscar.pack(pady=5)
        Label(frame_buscar, text="ID a Buscar:").pack(side=LEFT)
        Entry(frame_buscar, textvariable=self.c_id, width=10).pack(side=LEFT, padx=5)
        Button(frame_buscar, text="Buscar ID", command=self.buscar_camioneta).pack(side=LEFT)
        
        Label(self.wind, text="-- Editar Datos --").pack(pady=5)
        self.entry_form_camionetas()
        
        Button(self.wind, text="Actualizar Cambios", command=self.editar_camioneta).pack(pady=10)
        Button(self.wind, text="Regresar", command=self.menu_camionetas).pack(pady=5)

    def vista_camioneta_eliminar(self):
        self.limpiar_ventana()
        self.limpiar_campos_camioneta()
        Label(self.wind, text="ELIMINAR CAMIONETA").pack(pady=10)
        
        frame_buscar = Frame(self.wind)
        frame_buscar.pack(pady=5)
        Label(frame_buscar, text="ID a Buscar:").pack(side=LEFT)
        Entry(frame_buscar, textvariable=self.c_id, width=10).pack(side=LEFT, padx=5)
        Button(frame_buscar, text="Buscar ID", command=self.buscar_camioneta).pack(side=LEFT)
        
        self.entry_form_camionetas()
        
        # Label(self.wind, text="ID a Eliminar:").pack()
        # Entry(self.wind, textvariable=self.c_id).pack()
        
        Button(self.wind, text="Eliminar", command=self.eliminar_camioneta).pack(pady=10)
        Button(self.wind, text="Regresar", command=self.menu_camionetas).pack(pady=5)

    def buscar_camioneta(self):
        if not self.c_id.get():
            messagebox.showwarning("Alerta", "Escribe un ID primero")
            return
        
        dato = coches.Camionetas.buscar(self.c_id.get())
        if dato:
            self.c_marca.set(dato[1])
            self.c_color.set(dato[2])
            self.c_modelo.set(dato[3])
            self.c_vel.set(dato[4])
            self.c_hp.set(dato[5])
            self.c_plazas.set(dato[6])
            self.c_traccion.set(dato[7])
            self.c_cerrada.set(dato[8])
        else:
            messagebox.showerror("Error", "No se encontró ningún auto con ese ID")
            self.limpiar_campos_camioneta()
    
    def entry_form_camionetas(self):
        Label(self.wind, text="Marca:").pack()
        Entry(self.wind, textvariable=self.c_marca).pack()

        Label(self.wind, text="Color:").pack()
        Entry(self.wind, textvariable=self.c_color).pack()

        Label(self.wind, text="Modelo:").pack()
        Entry(self.wind, textvariable=self.c_modelo).pack()

        Label(self.wind, text="Velocidad:").pack()
        Entry(self.wind, textvariable=self.c_vel).pack()

        Label(self.wind, text="Potencia:").pack()
        Entry(self.wind, textvariable=self.c_hp).pack()

        Label(self.wind, text="Plazas:").pack()
        Entry(self.wind, textvariable=self.c_plazas).pack()
        
        Label(self.wind, text="Traccion:").pack()
        Entry(self.wind, textvariable=self.c_traccion).pack()
        
        Label(self.wind, text="Cerrada:").pack()
        Entry(self.wind, textvariable=self.c_cerrada).pack()
    
    def guardar_camioneta(self):
        res = coches.Camionetas.insertar(self.c_marca.get(), self.c_color.get(), self.c_modelo.get(), self.c_vel.get(), self.c_hp.get(), self.c_plazas.get(), self.c_traccion.get(), self.c_cerrada.get())
        Controlador.respuesta(res)
        if res: 
            self.limpiar_campos_camioneta()

    def editar_camioneta(self):
        res = coches.Camionetas.actualizar(self.c_marca.get(), self.c_color.get(), self.c_modelo.get(), self.c_vel.get(), self.c_hp.get(), self.c_plazas.get(), self.c_traccion.get(), self.c_cerrada.get())
        Controlador.respuesta(res)
        if res: 
            self.limpiar_campos_camioneta()

    def eliminar_camioneta(self):
        res=coches.Camionetas.eliminar(self.c_id.get())
        Controlador.respuesta(res)
        if res:
            self.limpiar_campos_camioneta()

    def limpiar_campos_camioneta(self):
        self.c_id.set(""); self.c_marca.set(""); self.c_color.set(""); self.c_modelo.set(""); self.c_vel.set(0); self.c_hp.set(0); self.c_plazas.set(0); self.c_traccion.set(""); self.c_cerrada.set("")

        # ------------CAMIONES----------
        
    def vista_camion_insertar(self):
        self.limpiar_ventana()
        self.limpiar_campos_camion()
        Label(self.wind, text="INSERTAR CAMION").pack(pady=10)
        self.entry_form_camiones()
        Button(self.wind, text="Guardar", command=self.guardar_camion).pack(pady=10)
        Button(self.wind, text="Regresar", command=self.menu_camiones).pack(pady=5)

    def vista_camion_consultar(self):
        self.limpiar_ventana()
        Label(self.wind, text="CONSULTA DE CAMION").pack(pady=10)
        
        lista = Listbox(self.wind, width=100, height=20)
        lista.pack(pady=10)
        
        registros = coches.Camiones.consultar()
        for fila in registros:
            lista.insert(END, f"ID:{fila[0]} | Marca:{fila[1]} | Color:{fila[2]} | Modelo:{fila[3]} | Velocidad:{fila[4]} | Caballaje:{fila[5]} | Plazas:{fila[6]} | Eje:{fila[7]} | Capacidad Carga:{fila[8]}")
            
        Button(self.wind, text="Regresar", command=self.menu_camiones).pack(pady=10)

    def vista_camion_actualizar(self):
        self.limpiar_ventana()
        self.limpiar_campos_camion()
        Label(self.wind, text="ACTUALIZAR CAMIONES").pack(pady=10)
        
        Label(self.wind, text="ID a Actualizar:").pack()
        Entry(self.wind, textvariable=self.t_id).pack()
        
        Label(self.wind, text="-- Nuevos Datos --").pack(pady=5)
        self.entry_form_camiones()
        
        Button(self.wind, text="Actualizar", command=self.editar_camion).pack(pady=10)
        Button(self.wind, text="Regresar", command=self.menu_camiones).pack(pady=5)

    def vista_camion_eliminar(self):
        self.limpiar_ventana()
        self.limpiar_campos_camion()
        Label(self.wind, text="ELIMINAR CAMION").pack(pady=10)
        
        Label(self.wind, text="ID a Eliminar:").pack()
        Entry(self.wind, textvariable=self.t_id).pack()
        
        Button(self.wind, text="Eliminar", command=self.eliminar_camion).pack(pady=10)
        Button(self.wind, text="Regresar", command=self.menu_camiones).pack(pady=5)
    

    def entry_form_camiones(self):
        Label(self.wind, text="Marca:").pack()
        Entry(self.wind, textvariable=self.t_marca).pack()

        Label(self.wind, text="Color:").pack()
        Entry(self.wind, textvariable=self.t_color).pack()

        Label(self.wind, text="Modelo:").pack()
        Entry(self.wind, textvariable=self.t_modelo).pack()

        Label(self.wind, text="Velocidad:").pack()
        Entry(self.wind, textvariable=self.t_vel).pack()

        Label(self.wind, text="Potencia:").pack()
        Entry(self.wind, textvariable=self.t_hp).pack()

        Label(self.wind, text="Plazas:").pack()
        Entry(self.wind, textvariable=self.t_plazas).pack()
        
        Label(self.wind, text="Traccion:").pack()
        Entry(self.wind, textvariable=self.t_ejes).pack()
        
        Label(self.wind, text="Cerrada:").pack()
        Entry(self.wind, textvariable=self.t_carga).pack()

    def guardar_camion(self):
        pass

    def editar_camion(self):
        pass

    def eliminar_camion(self):
        pass

    def limpiar_campos_camion(self):
        self.t_id.set(""); self.t_marca.set(""); self.t_color.set(""); self.t_modelo.set(""); self.t_vel.set(0); self.t_hp.set(0); self.t_plazas.set(0); self.t_ejes.set(0); self.t_carga.set(0)