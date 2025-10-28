import funciones
from usuarios import usuario
from notas import nota
import getpass

def main():
    opcion=True
    while opcion:
        funciones.borrarPantalla()
        opcion=funciones.menu_usurios()

        if opcion=="1" or opcion=="REGISTRO":
            funciones.borrarPantalla()
            print("\n \t ..:: Registro en el Sistema ::..")
            nombre=input("\t ¿Cual es tu nombre?: ").upper().strip()
            apellidos=input("\t ¿Cuales son tus apellidos?: ").upper().strip()
            email=input("\t Ingresa tu email: ").lower().strip()
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            resultado = usuario.registrar(nombre,apellidos,email,password)
            if resultado:
                print(f"\n\t{nombre} {apellidos} se registró correctamente, con el email: {email}")
            else:
                print("\n\t..::No fue posible insertar el registro, por favor intentelo de nuevo::..")
            funciones.esperarTecla()

        elif opcion == "2" or opcion.upper() == "LOGIN":
            funciones.borrarPantalla()
            print("\n \t ..:: Inicio de Sesión ::.. ")
            email = input("\t Ingresa tu E-mail: ").lower().strip()
            password = getpass.getpass("\t Ingresa tu contraseña: ").strip()
            registro = usuario.iniciar_sesion(email, password)
            if registro:
                menu_notas(registro[0], registro[1], registro[2])
            else:
                print(f"\n\t❌ Email y/o contraseña incorrectos. Inténtalo nuevamente.")
            funciones.esperarTecla()

        elif opcion=="3" or opcion=="SALIR": 
            print("Termino la Ejecución del Sistema")
            opcion=False
            funciones.esperarTecla()  
        else:
            print("Opcion no valida")
            opcion=True
            funciones.esperarTecla() 

def menu_notas(usuario_id,nombre,apellidos):
    opc=True
    while opc:
        funciones.borrarPantalla()
        print(f"\n \t \t \t Bienvenido {nombre} {apellidos}, has iniciado sesión ...")
        opcion=funciones.menu_notas()

        if opcion == '1' or opcion=="CREAR":
            funciones.borrarPantalla()
            print(f"\n \t .:: Crear Nota ::. ")
            titulo=input("\tTitulo: ").strip()
            descripcion=input("\tDescripción: ")
            #Agregar codigo
            respuesta=nota.crear(usuario_id, titulo, descripcion)
            if respuesta:
                print(f"..:: Se creo la nota {titulo} exitosamente ::..")
            else:
                print("..:: No fue posible crear la nota en este momento, vuelva a intentar ::..")
            funciones.esperarTecla()

        elif opcion == '2' or opcion.upper() == "MOSTRAR":
            funciones.borrarPantalla()
            lista_notas = nota.mostrar(usuario_id)
            if lista_notas:
                print("\n \U0001F50D  .:: Mostrar Notas ::. \n")  # 🔍
                print(f"{'|'}{'ID':<6}{'|'}{'Título':<20}{'|'}{'Descripción':<50}{'|'}{'Fecha':<20}{'|'}")
                print(f"{'-'*100}")
                for fila in lista_notas:
                    fecha_str = fila[4].strftime("%Y-%m-%d %H:%M:%S") if fila[4] else "Sin fecha"
                    print(f"{'|'}{fila[0]:<6}{'|'}{fila[2]:<20}{'|'}{fila[3]:<50}{'|'}{fecha_str:<20}{'|'}")
                print(f"{'-'*100}")
            else:
                print("ℹ️ No existen notas para mostrar.")
            funciones.esperarTecla()

        elif opcion == '3' or opcion.upper() == "CAMBIAR":
            funciones.borrarPantalla()
            lista_notas = nota.mostrar(usuario_id)
            if lista_notas:
                print("\n \U0001F58A️  .:: Modificar Notas ::. \n")  # 🖊️
                print(f"{'|'}{'ID':<6}{'|'}{'Título':<20}{'|'}{'Descripción':<50}{'|'}{'Fecha':<20}{'|'}")
                print(f"{'-'*100}")
                for fila in lista_notas:
                    fecha_str = fila[4].strftime("%Y-%m-%d %H:%M:%S") if fila[4] else "Sin fecha"
                    print(f"{'|'}{fila[0]:<6}{'|'}{fila[2]:<20}{'|'}{fila[3]:<50}{'|'}{fecha_str:<20}{'|'}")
                print(f"{'-'*100}")
                
                id_nota = input("\nIngrese el ID de la nota que deseas modificar: ").strip()
                confirmar = input(f"¿Estás seguro de modificar la nota con ID {id_nota}? (SI/NO): ").strip().lower()
                
                if confirmar == "si":
                    nuevo_titulo = input("Nuevo título: ").strip()
                    nueva_desc = input("Nueva descripción: ").strip()
                    respuesta = nota.cambiar(id_nota, nuevo_titulo, nueva_desc, usuario_id)
                    if respuesta:
                        print(f"\n✅ Nota actualizada exitosamente.")
                    else:
                        print("\n❌ No fue posible actualizar la nota. ¿El ID te pertenece?")
                else:
                    print("\nℹ️ Modificación cancelada.")
            else:
                print("ℹ️ No tienes notas para modificar.")
            funciones.esperarTecla()   

        elif opcion == '4' or opcion.upper() == "ELIMINAR":
            funciones.borrarPantalla()
            lista_notas = nota.mostrar(usuario_id)
            if lista_notas:
                print("\n 🗑️  .:: Eliminar Notas ::. \n")
                print(f"{'|'}{'ID':<6}{'|'}{'Título':<20}{'|'}{'Descripción':<50}{'|'}{'Fecha':<20}{'|'}")
                print(f"{'-'*100}")
                for fila in lista_notas:
                    fecha_str = fila[4].strftime("%Y-%m-%d %H:%M:%S") if fila[4] else "Sin fecha"
                    print(f"{'|'}{fila[0]:<6}{'|'}{fila[2]:<20}{'|'}{fila[3]:<50}{'|'}{fecha_str:<20}{'|'}")
                print(f"{'-'*100}")
                id_nota = input("\nIngrese el ID de la nota que deseas eliminar: ").strip()
                confirm = input(f"¿Estás seguro de eliminar la nota con ID {id_nota}? (SI/NO): ").strip().lower()
                if confirm == "si":
                    respuesta = nota.borrar(id_nota, usuario_id)
                    if respuesta:
                        print("\n✅ Nota eliminada exitosamente.")
                    else:
                        print("\n❌ No se pudo eliminar la nota. ¿El ID te pertenece?")
                else:
                    print("\nℹ️ Eliminación cancelada.")
            else:
                print("ℹ️ No tienes notas para eliminar.")
            funciones.esperarTecla()

        elif opcion == '5' or opcion.upper() == "SALIR":
            opc = False
        else:
            print("\n❗ Opción no válida. Inténtalo de nuevo.")
            funciones.esperarTecla()

if __name__ == "__main__":
    main()    


