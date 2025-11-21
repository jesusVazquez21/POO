from tkinter import *
from tkinter import messagebox
from model.operaciones import Operaciones
class Funciones:
    @staticmethod
    def respuesta(exito, accion="La acción"):
        if exito:
            messagebox.showinfo("Éxito", f"{accion} se realizó exitosamente.", icon="info")
        else:
            messagebox.showerror("Error", f"No se pudo completar {accion}. Por favor, verifique los datos.")

    @staticmethod
    def operaciones(n1, n2, signo):
        if signo=="+":
            ope=n1+n2
            tipo_ope="Suma"
        elif signo=="-":
            ope=n1-n2
            tipo_ope="Resta"
        elif signo=="x":
            ope=n1*n2
            tipo_ope="Multiplicacion"
        elif signo=="/":
            ope=n1/n2
            tipo_ope="Division"
        
        
        resultado_guardar = messagebox.askquestion(
                message=f"{n1}{signo}{n2} = {ope:.2f} \n\n ¿Deseas guardar en la base de datos?",
                icon="question"
            )

        if resultado_guardar == "yes":
            insertado = Operaciones.insertar(n1, n2, signo, ope)
            
            Funciones.respuesta(insertado, accion="La inserción")
            
        
    # @staticmethod
    # def operaciones(n1, n2, signo):
    #     if signo=="+":
    #         ope=n1+n2
    #         tipo_ope="Suma"
    #     elif signo=="-":
    #         ope=n1-n2
    #         tipo_ope="Resta"
    #     elif signo=="x":
    #         ope=n1*n2
    #         tipo_ope="Multiplicacion"
    #     elif signo=="/":
    #         ope=n1/n2
    #         tipo_ope="Division"
        
        
    #     resultado=messagebox.askquestion(message=f"{n1}{signo}{n2} = {ope} \n\n ¿Deseas guardar en la base de datos?", icon="question")
    #     if resultado=="yes":
    #         Operaciones.insertar(n1, n2, signo, ope)
            
            
            
            
            
            
            
            
            
            
    # @staticmethod
    # def mostrar_consulta(textarea):
    #     # ... (Esta función es la misma que ya teníamos, con los config 'normal' y 'disabled') ...
    #     textarea.config(state='normal')
    #     textarea.delete('1.0', END)
    #     datos = Operaciones.consultar()
    #     if datos: 
    #         header = f"{'ID':<5}{'Fecha':<25}{'Num1':<8}{'Num2':<8}{'Signo':<8}{'Resultado'}\n"
    #         linea = "-" * 80 + "\n"
    #         textarea.insert(END, header)
    #         textarea.insert(END, linea)
    #         for fila in datos:
    #             fila_str = f"{fila[0]:<5}{str(fila[1]):<25}{fila[2]:<8}{fila[3]:<8}{fila[4]:<8}{fila[5]}\n"
    #             textarea.insert(END, fila_str)
    #     else:
    #         textarea.insert(END, "No hay operaciones registradas.")
    #     textarea.config(state='disabled')

    # @staticmethod
    # def abrir_ventana_eliminar(textarea):
    #     """
    #     Abre una ventana nueva (Toplevel) para preguntar el ID a eliminar.
    #     """
    #     ventana_eliminar = Toplevel()
    #     ventana_eliminar.title("Eliminar Registro")
    #     ventana_eliminar.geometry("300x150")
        
    #     Label(ventana_eliminar, text="ID del registro a eliminar:").pack(pady=10)
        
    #     id_entry = Entry(ventana_eliminar, width=10)
    #     id_entry.pack(pady=5)
        
    #     def ejecutar_eliminacion():
    #         try:
    #             id_para_borrar = int(id_entry.get())
    #             if messagebox.askyesno("Confirmar", f"¿Seguro que deseas eliminar el ID {id_para_borrar}?"):
    #                 if Operaciones.eliminar(id_para_borrar):
    #                     messagebox.showinfo("Éxito", "Registro eliminado.")
    #                     ventana_eliminar.destroy() # Cierra la ventana emergente
    #                     Funciones.mostrar_consulta(textarea) # Refresca
    #                 else:
    #                     messagebox.showerror("Error", "No se pudo eliminar.")
    #         except ValueError:
    #             messagebox.showerror("Error", "ID inválido. Debe ser un número.")

    #     Button(ventana_eliminar, text="Eliminar", command=ejecutar_eliminacion).pack(pady=20)
    
    # @staticmethod
    # def suma(n1, n2):
    #     sumar=n1+n2
    #     messagebox.showinfo(title="Suma", message=f"{n1}+{n2} = {sumar}", icon="info")

    # @staticmethod
    # def resta(n1, n2):
    #     restar=n1-n2
    #     messagebox.showinfo(title="Resta", message=f"{n1}-{n2} = {restar}", icon="info")

    # @staticmethod
    # def multiplicar(n1, n2):
    #     multiplicacion=n1*n2
    #     messagebox.showinfo(title="Multiplicacion", message=f"{n1}*{n2} = {multiplicacion}", icon="info")

    # @staticmethod
    # def division(n1, n2):
    #     divisar=n1/n2
    #     messagebox.showinfo(title="Division", message=f"{n1}/{n2} = {divisar}", icon="info")

    
    