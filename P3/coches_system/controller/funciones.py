from tkinter import messagebox

class Controlador:
    
    @staticmethod
    def respuesta(exito, accion="La acción"):
        if exito:
            messagebox.showinfo("Éxito", f"{accion} se realizó exitosamente.", icon="info")
        else:
            messagebox.showerror("Error", f"No se pudo completar {accion}. Por favor, verifique los datos.")