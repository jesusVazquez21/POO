import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error

# -------------------------------
# Clase para la conexión a MySQL
# -------------------------------
class Database:
    def __init__(self, host, user, password, database):
        try:
            self.conn = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            self.cursor = self.conn.cursor()
            print("Conexión a BD exitosa.")
        except Error as e:
            messagebox.showerror("Error", f"No se pudo conectar a la BD: {e}")

    def fetch(self):
        self.cursor.execute("SELECT * FROM peliculas")
        return self.cursor.fetchall()

    def insert(self, titulo, director, anio):
        self.cursor.execute("INSERT INTO peliculas (titulo, director, anio) VALUES (%s, %s, %s)",
                            (titulo, director, anio))
        self.conn.commit()

    def update(self, id_peli, titulo, director, anio):
        self.cursor.execute("UPDATE peliculas SET titulo=%s, director=%s, anio=%s WHERE id=%s",
                            (titulo, director, anio, id_peli))
        self.conn.commit()

    def delete(self, id_peli):
        self.cursor.execute("DELETE FROM peliculas WHERE id=%s", (id_peli,))
        self.conn.commit()

# -------------------------------
# Clase para la interfaz gráfica
# -------------------------------
class PeliculasApp:
    def __init__(self, root):
        self.db = Database("localhost", "root", "", "db_peliculas")
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
    # Métodos CRUD
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

# -------------------------------
# Ejecución principal
# -------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = PeliculasApp(root)
    root.mainloop()