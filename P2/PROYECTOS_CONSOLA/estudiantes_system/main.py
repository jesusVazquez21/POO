from estudiantes.estudiante import Estudiante
from usuarios.usuario import Usuario
import os
import getpass

def borrarPantalla():
    os.system("cls")

def esperarTecla():
    input("\nPresiona ENTER para continuar...")


class App:
    def __init__(self):
        self.menu_principal()

    def menu_principal(self):
        while True:
            borrarPantalla()
            print("""
        .:: Sistema de Estudiantes ::.
            1.- Registro
            2.- Login
            3.- Salir
            """)
            opcion = input("\t Elige una opción: ").upper()

            if opcion in ['1', 'REGISTRO']:
                borrarPantalla()
                print("\n\t ..:: Registro en el Sistema ::..")
                nombre = input("\t Nombre: ")
                apellidos = input("\t Apellidos: ")
                email = input("\t Email: ")
                password = getpass.getpass("\t Contraseña: ")
                if Usuario.registrar(nombre, apellidos, email, password):
                    print(f"\n\t  Usuario {nombre} registrado correctamente.")
                else:
                    print("\n\t  Error al registrar el usuario.")
                esperarTecla()

            elif opcion in ['2', 'LOGIN']:
                borrarPantalla()
                print("\n\t ..:: Inicio de Sesión ::..")
                email = input("\t Email: ")
                password = getpass.getpass("\t Contraseña: ")
                usuario = Usuario.iniciar_sesion(email, password)
                if usuario:
                    print(f"\n\t Bienvenido {usuario[1]} {usuario[2]} 👋")
                    esperarTecla()
                    self.menu_estudiantes(usuario)
                else:
                    print("\n\t  Credenciales incorrectas.")
                    esperarTecla()

            elif opcion in ['3', 'SALIR']:
                print("\n\t  ¡Hasta luego!")
                break
            else:
                print("\n\t  Opción no válida.")
                esperarTecla()

    def menu_estudiantes(self, usuario):
        while True:
            borrarPantalla()
            print(f"\n\t Bienvenido {usuario[1]} {usuario[2]}")
            print("""
        .:: Menú Estudiantes ::.
            1.- Registrar 
            2.- Mostrar 
            3.- Actualizar 
            4.- Eliminar 
            5.- Cerrar Sesión
            """)
            opcion = input("\t Elige una opción: ").upper()

            if opcion == '1':
                borrarPantalla()
                nombre = input("\t Nombre del estudiante: ")
                nota = float(input("\t Nota: "))
                if Estudiante.insertar(nombre, nota):
                    print(f"\n\t  Estudiante {nombre} registrado correctamente.")
                else:
                    print("\n\t  Error al registrar el estudiante.")
                esperarTecla()

            elif opcion == '2':
                borrarPantalla()
                registros = Estudiante.consultar()
                if registros:
                    for fila in registros:
                        estado = "Aprobado " if fila[2] >= 7 else "Reprobado "
                        print(f"ID: {fila[0]} | Nombre: {fila[1]} | Nota: {fila[2]} | {estado}")
                else:
                    print("\n\t No hay estudiantes registrados.")
                esperarTecla()

            elif opcion == '3':
                borrarPantalla()
                id = input("\t ID del estudiante: ")
                nombre = input("\t Nuevo nombre: ")
                nota = float(input("\t Nueva nota: "))
                if Estudiante.actualizar(id, nombre, nota):
                    print("\n\t  Estudiante actualizado correctamente.")
                else:
                    print("\n\t  Error al actualizar el estudiante.")
                esperarTecla()

            elif opcion == '4':
                borrarPantalla()
                id = input("\t ID del estudiante a eliminar: ")
                if Estudiante.eliminar(id):
                    print("\n\t  Estudiante eliminado correctamente.")
                else:
                    print("\n\t  No se pudo eliminar el estudiante.")
                esperarTecla()

            elif opcion == '5':
                break
            else:
                print("\n\t  Opción no válida.")
                esperarTecla()


if __name__ == "__main__":
    app = App()