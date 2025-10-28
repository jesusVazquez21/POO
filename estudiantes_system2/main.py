from estudiantes.estudiante import Estudiante
from usuarios.usuario import Usuario
import os
import getpass

class App:
    def __init__(self):
        self.main()
        
    def borrarPantalla(self):
        os.system("cls")

    def esperarTecla(self):
        input("\nPresiona ENTER para continuar...")

    def menu_registro(self):
        while True:
            self.borrarPantalla()
            print("""
        .:: Sistema de Estudiantes ::.
            1.- Registro
            2.- Login
            3.- Salir
            """)
            opcion = input("\t Elige una opción: ").upper()

            if opcion in ['1', 'REGISTRO']:
                self.borrarPantalla()
                print("\n\t ..:: Registro en el Sistema ::..")
                nombre = input("\t Nombre: ")
                apellidos = input("\t Apellidos: ")
                email = input("\t Email: ")
                password = getpass.getpass("\t Contraseña: ")
                if Usuario.registrar(nombre, apellidos, email, password):
                    print(f"\n\t  Usuario {nombre} registrado correctamente.")
                else:
                    print("\n\t  Error al registrar el usuario.")
                self.esperarTecla()

            elif opcion in ['2', 'LOGIN']:
                self.borrarPantalla()
                print("\n\t ..:: Inicio de Sesión ::..")
                email = input("\t Email: ")
                password = getpass.getpass("\t Contraseña: ")
                usuario = Usuario.iniciar_sesion(email, password)
                if usuario:
                    print(f"\n\t Bienvenido {usuario[1]} {usuario[2]} 👋")
                    self.esperarTecla()
                    self.menu_estudiantes(usuario)
                else:
                    print("\n\t  Credenciales incorrectas.")
                    self.esperarTecla()

            elif opcion in ['3', 'SALIR']:
                print("\n\t  ¡Hasta luego!")
                break
            else:
                print("\n\t  Opción no válida.")
                self.esperarTecla()

    def datos_estudiante(self, tipo):
        self.borrarPantalla()
        print(f"\n\t.. Ingresar los datos del estudiante :{tipo}")
        nombre=input("Nombre: ").upper()
        nota=float(input("Nota: "))
        return nombre, nota
    
    def menu_acciones(self, tipo):
        print(f"\n\t ..:: MENU DE {tipo} ::..")
        print("\n\t 1.-Insertar \n\t 2.-Consultar \n\t 3.-Actualizar \n\t 4.-Eliminar \n\t 5.-Regresar")
        opcion=input("\n\t Selecciona una opcion: ").upper().strip()
        return opcion
    
    def respuesta_sql(self, respuesta):
        if respuesta:
            print("\n\t\t...Accion realizada con éxito!...")
            self.esperarTecla()
        else:
            print("\n\t...No fue posible realizar la accion. Vuelva a intentar ...") 
            self.esperarTecla()
    
    def menu_estudiantes(self):
        while True:
            self.borrarPantalla()
            opcion=self.menu_acciones("Estudiante")
            if opcion == '1':
                self.borrarPantalla()
                nombre = input("\t Nombre del estudiante: ")
                nota = float(input("\t Nota: "))
                respuesta=Estudiante.insertar(nombre, nota)
                self.respuesta_sql(respuesta)

            elif opcion == '2':
                self.borrarPantalla()
                registros = Estudiante.consultar()
                if registros:
                    for fila in registros:
                        estado = "Aprobado " if fila[2] >= 7 else "Reprobado "
                        print(f"ID: {fila[0]} | Nombre: {fila[1]} | Nota: {fila[2]} | {estado}")
                else:
                    print("\n\t No hay estudiantes registrados.")
                self.esperarTecla()

            elif opcion == '3':
                self.borrarPantalla()
                id = input("\t ID del estudiante: ")
                nombre = input("\t Nuevo nombre: ")
                nota = float(input("\t Nueva nota: "))
                if Estudiante.actualizar(nombre, nota, id):
                    print("\n\t  Estudiante actualizado correctamente.")
                else:
                    print("\n\t  Error al actualizar el estudiante.")
                self.esperarTecla()

            elif opcion == '4':
                self.borrarPantalla()
                id = input("\t ID del estudiante a eliminar: ")
                respuesta=Estudiante.eliminar(id)
                self.respuesta_sql(respuesta)

            elif opcion == '5':
                break
            else:
                print("\n\t ... Opción no válida. Intenta de nuevo ...")
                self.esperarTecla()

    def main(self):
        opcion=True
        while opcion:
            self.borrarPantalla()
            opcion=input("\n\t\t ::: Menu Principal ::.\n\t1.- Estudiante \n\t2.-Salir\n\t Elige un opción: ").lower().strip()
            match opcion:
                case "1":
                    self.menu_estudiantes()
                    self.esperarTecla()
                case "2":
                    self.borrarPantalla()
                    input("\n\t\tSalir del Sistema")
                    opcion=False   
                case _:
                    input("Opcion invalidad ... vuelva a intertarlo ... ")      

if __name__ == "__main__":
    app = App()