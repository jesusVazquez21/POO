from tkinter import *
from tkinter import ttk
from model import coches
from controller.funciones import Controlador

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
        Button(self.wind, text="2. Camionetas", command="self.menu_camionetas", width=30).pack(pady=5)
        Button(self.wind, text="3. Camiones", command="self.menu_camiones", width=30).pack(pady=5)
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
        pass

    def menu_camiones(self):
        pass

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
            lista.insert(END, f"ID:{fila[0]} | Marca: {fila[1]} | Color: {fila[2]} | Modelo{fila[3]} | Vel:{fila[4]} | Caballaje:{fila[5]} | Plazas:{fila[6]}")
            
        Button(self.wind, text="Regresar", command=self.menu_autos).pack(pady=10)

    def vista_auto_actualizar(self):
        self.limpiar_ventana()
        self.limpiar_campos_auto()
        Label(self.wind, text="ACTUALIZAR AUTO").pack(pady=10)
        
        Label(self.wind, text="ID a Actualizar:").pack()
        Entry(self.wind, textvariable=self.a_id).pack()
        
        Label(self.wind, text="-- Nuevos Datos --").pack(pady=5)
        self.helper_form_autos()
        
        Button(self.wind, text="Actualizar", command=self.editar_auto).pack(pady=10)
        Button(self.wind, text="Regresar", command=self.menu_autos).pack(pady=5)

    def vista_auto_eliminar(self):
        self.limpiar_ventana()
        self.limpiar_campos_auto()
        Label(self.wind, text="ELIMINAR AUTO").pack(pady=10)
        
        Label(self.wind, text="ID a Eliminar:").pack()
        Entry(self.wind, textvariable=self.a_id).pack()
        
        Button(self.wind, text="Eliminar", command=self.eliminar_auto).pack(pady=10)
        Button(self.wind, text="Regresar", command=self.menu_autos).pack(pady=5)

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
        pass

    def eliminar_auto(self):
        pass
    
    def limpiar_campos_auto(self):
        self.a_id.set(""); self.a_marca.set(""); self.a_color.set(""); self.a_modelo.set(""); self.a_vel.set(0); self.a_hp.set(0); self.a_plazas.set(0)

    #----------CAMIONETAS---------------
    
    def vista_camioneta_insertar(self):
        pass

    def vista_camioneta_consultar(self):
        pass

    def vista_camioneta_actualizar(self):
        pass

    def vista_camioneta_eliminar(self):
        pass

    def helper_form_camionetas(self):
        pass
    
    def guardar_camioneta(self):
        pass

    def editar_camioneta(self):
        pass

    def eliminar_camioneta(self):
        pass

    def limpiar_campos_camioneta(self):
        self.c_id.set(""); self.c_marca.set(""); self.c_color.set(""); self.c_modelo.set(""); self.c_vel.set(0); self.c_hp.set(0); self.c_plazas.set(0); self.c_traccion.set(""); self.c_cerrada.set("")

        # ------------CAMIONES----------
        
    def vista_camion_insertar(self):
        pass

    def vista_camion_consultar(self):
        pass

    def vista_camion_actualizar(self):
        pass

    def vista_camion_eliminar(self):
        pass

    def helper_form_camiones(self):
        pass

    def guardar_camion(self):
        pass

    def editar_camion(self):
        pass

    def eliminar_camion(self):
        pass

    def limpiar_campos_camion(self):
        self.t_id.set(""); self.t_marca.set(""); self.t_color.set(""); self.t_modelo.set(""); self.t_vel.set(0); self.t_hp.set(0); self.t_plazas.set(0); self.t_ejes.set(0); self.t_carga.set(0)