
from tkinter import messagebox
from model.usuario import Usuario
from model.nota import Nota

class Controlador:
    
    @staticmethod
    def respuesta(exito, accion="La acción"):
        if exito:
            messagebox.showinfo("Éxito", f"{accion} se realizó exitosamente.", icon="info")
        else:
            messagebox.showerror("Error", f"No se pudo completar {accion}. Por favor, verifique los datos.")
            
    @staticmethod
    def registro(nombre, apellidos, email, password):
        resultado = Usuario.registrar(nombre, apellidos, email, password)
        if resultado:
            messagebox.showinfo(title="Registro Exitoso", message=f"{nombre} registrado correctamente.")
            return True
        else:
            messagebox.showerror(title="Error", message="No se pudo registrar.")
            return False

    @staticmethod
    def iniciarsesion(email, password):
        registro = Usuario.iniciar_sesion(email, password)
        if registro:
            messagebox.showinfo(title="Bienvenido", message=f"Bienvenido {registro[1]} {registro[2]}")
            return registro 
        else:
            messagebox.showerror(title="Error", message="Email o contraseña incorrectos.")
            return None

    @staticmethod
    def crearNota(usuario_id, titulo, descripcion):
        resultado = Nota.crear(usuario_id, titulo, descripcion)
        
        Controlador.respuesta(resultado, "Crear nota")
        return resultado
    
    @staticmethod
    def obtenerNotas(usuario_id):
        notas = Nota.mostrar(usuario_id)
        return notas
    
    @staticmethod
    def actualizarNota(id_nota, nuevo_titulo, nueva_descripcion):
        resultado = Nota.actualizar(id_nota, nuevo_titulo, nueva_descripcion)
        
        Controlador.respuesta(resultado, "La actualización de la nota")
        return resultado

    @staticmethod
    def eliminarNota(id_nota):
        resultado = Nota.eliminar(id_nota)
        
        Controlador.respuesta(resultado, "La eliminación de la nota")
        return resultado





















# from tkinter import messagebox
# from tkinter import *
# from model.usuario import Usuario
# from model.nota import Nota
# from view import view1 


# class Controlador:
    
#     @staticmethod
#     def respuesta(exito, accion="La acción"):
#         if exito:
#             messagebox.showinfo("Éxito", f"{accion} se realizó exitosamente.", icon="info")
#         else:
#             messagebox.showerror("Error", f"No se pudo completar {accion}. Por favor, verifique los datos.")

    
#     @staticmethod
#     def registro(nombre, apellidos, email, password):
#         resultado=Usuario.registrar(nombre, apellidos, email, password)
#         if resultado:
#                 messagebox.showinfo(icon="info", message=f"\n\t {nombre} {apellidos}, se registro correctamente, con el email: {email}", title="Registro Exitoso")
#         else:
#                 messagebox.showerror(icon="error", message=f"\n\t ** Por favor intentelo de nuevo, no fue posible insertar el registro ** ...", title="Usuarios")
    
#     @staticmethod
#     def iniciarsesion(ventana, email, password):
#         registro=Usuario.iniciar_sesion(email,password)
#         if registro:
#                 messagebox.showinfo(icon="info", message=f"Usuario: {registro[1]} {registro[2]}  Iniciaste sesion Correctamente", title="Usuarios")
#                 view1.View.menuNotas(ventana, registro[0], registro[1], registro[2])
#         else:
#             messagebox.showerror(icon="error", message=f"\n\t Email y/o contraseña incorrectas... vuelva a intentarlo ...")

#     @staticmethod
#     def crearNota(usuario_id, titulo, descripcion):
#         resultado=Nota.crear(usuario_id, titulo, descripcion)
#         Controlador.respuesta(resultado)
        # if resultado:
        #         messagebox.showinfo(icon="info", message=f"\n\t La nota {titulo} se creo correctamente", title="Registro Exitoso")
        # else:
        #         messagebox.showerror(icon="error", message=f"\n\t ** Por favor intentelo de nuevo, no fue posible insertar el registro ** ...", title="Usuarios")
    