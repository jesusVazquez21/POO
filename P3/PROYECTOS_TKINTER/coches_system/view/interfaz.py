from tkinter import *
from tkinter import ttk
from model import coches
from controller.funciones import Controlador

class Vista:
    def __init__(self, window):
        self.wind = window
        self.wind.title("Sistema de Gestión de Vehículos - Menú Principal")
        self.wind.geometry("1100x650")
        self.wind.resizable(False, False)
        
        self.menu_principal()

    def limpiar_ventana(self):
        for widget in self.wind.winfo_children():
            widget.destroy()

    def menu_principal(self):
        self.limpiar_ventana()
        self.wind.title("Sistema de Gestión de Vehículos - Menú Principal")

        # Contenedor para centrar
        frame_menu = Frame(self.wind)
        frame_menu.pack(expand=True)

        Label(frame_menu, text="..:: MENÚ PRINCIPAL ::..", font=("Arial", 20, "bold")).pack(pady=30)
        
        Button(frame_menu, text="1. Gestión de Autos", width=25, height=2, command=self.vista_autos ).pack(pady=10)
        Button(frame_menu, text="2. Gestión de Camionetas", width=25, height=2, command=self.vista_camionetas).pack(pady=10)
        Button(frame_menu, text="3. Gestión de Camiones", width=25, height=2, command=self.vista_camiones).pack(pady=10)
        
        Button(frame_menu, text="Salir", command=self.wind.quit, font=("Arial", 12)).pack(pady=30)

    # ==========================================
    #             VISTA: AUTOS
    # ==========================================
    def vista_autos(self):
        self.limpiar_ventana()
        self.wind.title("Gestión de Autos")

        # Título
        Label(self.wind, text="..:: GESTIÓN DE AUTOS ::..", font=("Arial", 16, "bold")).pack(pady=10)

        # Formulario
        frame = LabelFrame(self.wind, text="Datos del Auto", padx=10, pady=10)
        frame.pack(padx=20, pady=5, fill="x")

        # Variables de instancia (para poder usarlas en guardar/editar)
        self.a_id = StringVar()
        self.a_marca = StringVar()
        self.a_color = StringVar()
        self.a_modelo = StringVar()
        self.a_vel = IntVar()
        self.a_hp = IntVar()
        self.a_plazas = IntVar()

        # Grid de entradas
        entries = [
            ("Marca:", self.a_marca, 0, 0), ("Color:", self.a_color, 0, 2), ("Modelo:", self.a_modelo, 0, 4),
            ("Velocidad:", self.a_vel, 1, 0), ("Caballaje:", self.a_hp, 1, 2), ("Plazas:", self.a_plazas, 1, 4)
        ]
        for txt, var, r, c in entries:
            Label(frame, text=txt).grid(row=r, column=c, sticky=E, padx=5, pady=5)
            Entry(frame, textvariable=var).grid(row=r, column=c+1, padx=5, pady=5)

        # Botones de Acción
        self.crear_botones_crud(self.wind, self.guardar_auto, self.editar_auto, self.eliminar_auto, self.limpiar_campos_auto)

        # Tabla
        cols = ("ID", "Marca", "Color", "Modelo", "Velocidad", "HP", "Plazas")
        self.tree_autos = self.crear_tabla(self.wind, cols, self.seleccionar_auto)
        self.cargar_autos()

        # Botón Volver
        Button(self.wind, text="<< Volver al Menú", command=self.menu_principal, bg="gray", fg="white").pack(pady=10, side=BOTTOM, anchor=W, padx=20)

    # --- Lógica Autos ---
    def cargar_autos(self):
        self.limpiar_tabla_visual(self.tree_autos)
        for dato in coches.Autos.consultar():
            self.tree_autos.insert('', END, values=dato)

    def guardar_auto(self):
        res = coches.Autos.insertar(self.a_marca.get(), self.a_color.get(), self.a_modelo.get(), self.a_vel.get(), self.a_hp.get(), self.a_plazas.get())
        Controlador.Controlador.respuesta(res, "Auto guardado correctamente")
        if res: self.cargar_autos(); self.limpiar_campos_auto()

    def editar_auto(self):
        if not self.a_id.get(): 
            return
        res = coches.Autos.actualizar(self.a_id.get(), self.a_marca.get(), self.a_color.get(), self.a_modelo.get(), self.a_vel.get(), self.a_hp.get(), self.a_plazas.get())
        Controlador.Controlador.respuesta(res, "Auto actualizado")
        if res: 
            self.cargar_autos(); self.limpiar_campos_auto()

    def eliminar_auto(self):
        if not self.a_id.get(): 
            return
        res = coches.Autos.eliminar(self.a_id.get())
        Controlador.Controlador.respuesta(res, "Auto eliminado")
        if res: 
            self.cargar_autos(); 
            self.limpiar_campos_auto()

    def seleccionar_auto(self, event):
        item = self.tree_autos.focus()
        val = self.tree_autos.item(item, 'values')
        if val:
            self.a_id.set(val[0]); self.a_marca.set(val[1]); self.a_color.set(val[2])
            self.a_modelo.set(val[3]); self.a_vel.set(val[4]); self.a_hp.set(val[5]); self.a_plazas.set(val[6])

    def limpiar_campos_auto(self):
        self.a_id.set(""); self.a_marca.set(""); self.a_color.set(""); self.a_modelo.set("")
        self.a_vel.set(0); self.a_hp.set(0); self.a_plazas.set(0)


    # ==========================================
    #           VISTA: CAMIONETAS
    # ==========================================
    def vista_camionetas(self):
        self.limpiar_ventana()
        self.wind.title("Gestión de Camionetas")

        Label(self.wind, text="..:: GESTIÓN DE CAMIONETAS ::..", font=("Arial", 16, "bold")).pack(pady=10)

        frame = LabelFrame(self.wind, text="Datos de la Camioneta", padx=10, pady=10)
        frame.pack(padx=20, pady=5, fill="x")

        # Variables
        self.c_id = StringVar()
        self.c_marca = StringVar()
        self.c_color = StringVar()
        self.c_modelo = StringVar()
        self.c_vel = IntVar()
        self.c_hp = IntVar()
        self.c_plazas = IntVar()
        self.c_traccion = StringVar()
        self.c_cerrada = StringVar()

        # Grid inputs
        entries = [
            ("Marca:", self.c_marca, 0, 0), ("Color:", self.c_color, 0, 2), ("Modelo:", self.c_modelo, 0, 4),
            ("Velocidad:", self.c_vel, 1, 0), ("Caballaje:", self.c_hp, 1, 2), ("Plazas:", self.c_plazas, 1, 4),
            ("Tracción:", self.c_traccion, 2, 0)
        ]
        for txt, var, r, c in entries:
            Label(frame, text=txt).grid(row=r, column=c, sticky=E, padx=5, pady=5)
            Entry(frame, textvariable=var).grid(row=r, column=c+1, padx=5, pady=5)

        Label(frame, text="¿Cerrada?:").grid(row=2, column=2, sticky=E, padx=5, pady=5)
        combo = ttk.Combobox(frame, textvariable=self.c_cerrada, values=["SI", "NO"], state="readonly")
        combo.grid(row=2, column=3, padx=5, pady=5)
        combo.current(0)

        self.crear_botones_crud(self.wind, self.guardar_camioneta, self.editar_camioneta, self.eliminar_camioneta, self.limpiar_campos_camioneta)

        cols = ("ID", "Marca", "Color", "Modelo", "Velocidad", "HP", "Plazas", "Tracción", "Cerrada")
        self.tree_camionetas = self.crear_tabla(self.wind, cols, self.seleccionar_camioneta)
        self.cargar_camionetas()

        Button(self.wind, text="<< Volver al Menú", command=self.menu_principal, bg="gray", fg="white").pack(pady=10, side=BOTTOM, anchor=W, padx=20)

    # --- Lógica Camionetas ---
    def cargar_camionetas(self):
        self.limpiar_tabla_visual(self.tree_camionetas)
        for dato in coches.Camionetas.consultar():
            self.tree_camionetas.insert('', END, values=dato)

    def guardar_camioneta(self):
        res = coches.Camionetas.insertar(self.c_marca.get(), self.c_color.get(), self.c_modelo.get(), self.c_vel.get(), self.c_hp.get(), self.c_plazas.get(), self.c_traccion.get(), self.c_cerrada.get())
        Controlador.Controlador.respuesta(res, "Camioneta guardada")
        if res: self.cargar_camionetas(); self.limpiar_campos_camioneta()

    def editar_camioneta(self):
        if not self.c_id.get(): return
        res = coches.Camionetas.actualizar(self.c_id.get(), self.c_marca.get(), self.c_color.get(), self.c_modelo.get(), self.c_vel.get(), self.c_hp.get(), self.c_plazas.get(), self.c_traccion.get(), self.c_cerrada.get())
        Controlador.Controlador.respuesta(res, "Camioneta actualizada")
        if res: self.cargar_camionetas(); self.limpiar_campos_camioneta()

    def eliminar_camioneta(self):
        if not self.c_id.get(): return
        res = coches.Camionetas.eliminar(self.c_id.get())
        Controlador.Controlador.respuesta(res, "Camioneta eliminada")
        if res: self.cargar_camionetas(); self.limpiar_campos_camioneta()

    def seleccionar_camioneta(self, event):
        item = self.tree_camionetas.focus()
        val = self.tree_camionetas.item(item, 'values')
        if val:
            self.c_id.set(val[0]); self.c_marca.set(val[1]); self.c_color.set(val[2]); self.c_modelo.set(val[3])
            self.c_vel.set(val[4]); self.c_hp.set(val[5]); self.c_plazas.set(val[6]); self.c_traccion.set(val[7]); self.c_cerrada.set(val[8])

    def limpiar_campos_camioneta(self):
        self.c_id.set(""); self.c_marca.set(""); self.c_color.set(""); self.c_modelo.set("")
        self.c_vel.set(0); self.c_hp.set(0); self.c_plazas.set(0); self.c_traccion.set("")


    # ==========================================
    #             VISTA: CAMIONES
    # ==========================================
    def vista_camiones(self):
        self.limpiar_ventana()
        self.wind.title("Gestión de Camiones")
        
        Label(self.wind, text="..:: GESTIÓN DE CAMIONES ::..", font=("Arial", 16, "bold")).pack(pady=10)

        frame = LabelFrame(self.wind, text="Datos del Camión", padx=10, pady=10)
        frame.pack(padx=20, pady=5, fill="x")

        # Variables
        self.t_id = StringVar()
        self.t_marca = StringVar()
        self.t_color = StringVar()
        self.t_modelo = StringVar()
        self.t_vel = IntVar()
        self.t_hp = IntVar()
        self.t_plazas = IntVar()
        self.t_ejes = IntVar()
        self.t_carga = IntVar()

        # Grid inputs
        entries = [
            ("Marca:", self.t_marca, 0, 0), ("Color:", self.t_color, 0, 2), ("Modelo:", self.t_modelo, 0, 4),
            ("Velocidad:", self.t_vel, 1, 0), ("Caballaje:", self.t_hp, 1, 2), ("Plazas:", self.t_plazas, 1, 4),
            ("No. Ejes:", self.t_ejes, 2, 0), ("Carga (Kg):", self.t_carga, 2, 2)
        ]
        for txt, var, r, c in entries:
            Label(frame, text=txt).grid(row=r, column=c, sticky=E, padx=5, pady=5)
            Entry(frame, textvariable=var).grid(row=r, column=c+1, padx=5, pady=5)

        self.crear_botones_crud(self.wind, self.guardar_camion, self.editar_camion, self.eliminar_camion, self.limpiar_campos_camion)
        
        cols = ("ID", "Marca", "Color", "Modelo", "Velocidad", "HP", "Plazas", "Ejes", "Carga")
        self.tree_camiones = self.crear_tabla(self.wind, cols, self.seleccionar_camion)
        self.cargar_camiones()

        Button(self.wind, text="<< Volver al Menú", command=self.menu_principal, bg="gray", fg="white").pack(pady=10, side=BOTTOM, anchor=W, padx=20)

    # --- Lógica Camiones ---
    def cargar_camiones(self):
        self.limpiar_tabla_visual(self.tree_camiones)
        for dato in coches.Camiones.consultar():
            self.tree_camiones.insert('', END, values=dato)

    def guardar_camion(self):
        res = coches.Camiones.insertar(self.t_marca.get(), self.t_color.get(), self.t_modelo.get(), self.t_vel.get(), self.t_hp.get(), self.t_plazas.get(), self.t_ejes.get(), self.t_carga.get())
        Controlador.Controlador.respuesta(res, "Camión guardado")
        if res: self.cargar_camiones(); self.limpiar_campos_camion()

    def editar_camion(self):
        if not self.t_id.get(): return
        res = coches.Camiones.actualizar(self.t_id.get(), self.t_marca.get(), self.t_color.get(), self.t_modelo.get(), self.t_vel.get(), self.t_hp.get(), self.t_plazas.get(), self.t_ejes.get(), self.t_carga.get())
        Controlador.Controlador.respuesta(res, "Camión actualizado")
        if res: self.cargar_camiones(); self.limpiar_campos_camion()

    def eliminar_camion(self):
        if not self.t_id.get(): return
        res = coches.Camiones.eliminar(self.t_id.get())
        Controlador.Controlador.respuesta(res, "Camión eliminado")
        if res: self.cargar_camiones(); self.limpiar_campos_camion()

    def seleccionar_camion(self, event):
        item = self.tree_camiones.focus()
        val = self.tree_camiones.item(item, 'values')
        if val:
            self.t_id.set(val[0]); self.t_marca.set(val[1]); self.t_color.set(val[2]); self.t_modelo.set(val[3])
            self.t_vel.set(val[4]); self.t_hp.set(val[5]); self.t_plazas.set(val[6]); self.t_ejes.set(val[7]); self.t_carga.set(val[8])

    def limpiar_campos_camion(self):
        self.t_id.set(""); self.t_marca.set(""); self.t_color.set(""); self.t_modelo.set("")
        self.t_vel.set(0); self.t_hp.set(0); self.t_plazas.set(0); self.t_ejes.set(0); self.t_carga.set(0)


    # ==========================================
    #       HERRAMIENTAS (HELPERS)
    # ==========================================
    def crear_botones_crud(self, parent, cmd_guardar, cmd_editar, cmd_eliminar, cmd_limpiar):
        f = Frame(parent)
        f.pack(pady=5)
        Button(f, text="Guardar", command=cmd_guardar ).pack(side=LEFT, padx=10)
        Button(f, text="Actualizar", command=cmd_editar).pack(side=LEFT, padx=10)
        Button(f, text="Eliminar", command=cmd_eliminar ).pack(side=LEFT, padx=10)
        Button(f, text="Limpiar Campos", command=cmd_limpiar).pack(side=LEFT, padx=10)

    def crear_tabla(self, parent, cols, cmd_select):
        frame_tabla = Frame(parent)
        frame_tabla.pack(padx=20, pady=10, fill=BOTH, expand=True)

        tree = ttk.Treeview(frame_tabla, columns=cols, show='headings')
        for col in cols:
            tree.heading(col, text=col)
            tree.column(col, width=90, anchor=CENTER)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(frame_tabla, orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        
        tree.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        tree.bind("<<TreeviewSelect>>", cmd_select)
        return tree

    def limpiar_tabla_visual(self, tree):
        for item in tree.get_children():
            tree.delete(item)