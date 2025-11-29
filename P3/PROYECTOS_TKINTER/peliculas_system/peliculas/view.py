import tkinter as tk
from tkinter import ttk, messagebox
from peliculas import model


# -------------------------------
# Clase para la interfaz gráfica --VISTA--
# -------------------------------
class PeliculasApp:
    def __init__(self, root):
        self.db = model.Database("localhost", "root", "", "db_peliculas")
        self.root = root
        self.root.title("Gestor de Películas")
        self.root.geometry("650x400")

        # Variables
        self.titulo_var = tk.StringVar()
        self.director_var = tk.StringVar()
        self.anio_var = tk.StringVar()

        # Frame formulario
        form_frame = tk.Frame(self.root)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Título").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(form_frame, textvariable=self.titulo_var).grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Director").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(form_frame, textvariable=self.director_var).grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Año").grid(row=2, column=0, padx=5, pady=5)
        tk.Entry(form_frame, textvariable=self.anio_var).grid(row=2, column=1, padx=5, pady=5)

        # Botones
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Agregar", command=self.agregar_pelicula).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Modificar", command=self.modificar_pelicula).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Eliminar", command=self.eliminar_pelicula).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Limpiar", command=self.limpiar_campos).grid(row=0, column=3, padx=5)

        # Tabla
        self.tree = ttk.Treeview(self.root, columns=("ID", "Título", "Director", "Año"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Título", text="Título")
        self.tree.heading("Director", text="Director")
        self.tree.heading("Año", text="Año")
        self.tree.pack(fill="both", expand=True)
        self.tree.bind("<ButtonRelease-1>", self.seleccionar_pelicula)

        self.mostrar_peliculas()

    # -------------------------------
    # Métodos CRUD CONTROLADOR
    # -------------------------------
    def mostrar_peliculas(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for row in self.db.fetch():
            self.tree.insert("", tk.END, values=row)

    def agregar_pelicula(self):
        if self.titulo_var.get() and self.director_var.get() and self.anio_var.get():
            self.db.insert(self.titulo_var.get(), self.director_var.get(), self.anio_var.get())
            self.mostrar_peliculas()
            self.limpiar_campos()
        else:
            messagebox.showwarning("Atención", "Todos los campos son obligatorios.")

    def modificar_pelicula(self):
        selected = self.tree.focus()
        if selected:
            valores = self.tree.item(selected, "values")
            id_peli = valores[0]
            self.db.update(id_peli, self.titulo_var.get(), self.director_var.get(), self.anio_var.get())
            self.mostrar_peliculas()
            self.limpiar_campos()
        else:
            messagebox.showwarning("Atención", "Selecciona una película para modificar.")

    def eliminar_pelicula(self):
        selected = self.tree.focus()
        if selected:
            valores = self.tree.item(selected, "values")
            id_peli = valores[0]
            self.db.delete(id_peli)
            self.mostrar_peliculas()
            self.limpiar_campos()
        else:
            messagebox.showwarning("Atención", "Selecciona una película para eliminar.")

    def seleccionar_pelicula(self, event):
        selected = self.tree.focus()
        if selected:
            valores = self.tree.item(selected, "values")
            self.titulo_var.set(valores[1])
            self.director_var.set(valores[2])
            self.anio_var.set(valores[3])

    def limpiar_campos(self):
        self.titulo_var.set("")
        self.director_var.set("")
        self.anio_var.set("")

