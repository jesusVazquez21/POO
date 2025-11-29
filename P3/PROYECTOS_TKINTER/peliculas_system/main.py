import tkinter as tk
from peliculas import view

# -------------------------------
# Ejecución principal
# -------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = view.PeliculasApp(root)
    root.mainloop()