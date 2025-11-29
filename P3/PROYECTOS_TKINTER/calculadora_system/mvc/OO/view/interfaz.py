'''
Crear una calculadora: 
1.- Dos campos de texto
2.- 4 Botones para las Operaciones
3.- Mostrar el resultado
4.- Programacion de forma Orientada a Objetos
5.-Considerar MVC
'''

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
from controller.funciones import Funciones
from model.operaciones import Operaciones

class Vista:
    def __init__(self,ventana):
        ventana.title("Calculadora")
        ventana.geometry("700x600")
        ventana.resizable(False,False)
        ventana.config(bg="#ffffff")
        self.valores = None
        self.interfaz_principal(ventana)

    @staticmethod
    def menuPrincipal(ventana):
        menuBar = Menu(ventana)
        ventana.config(menu=menuBar)    
        archivoMenu = Menu(menuBar , tearoff=0)
        menuBar.add_cascade(label="Archivo" , menu=archivoMenu)
        archivoMenu.add_command(label="Agregar",command=lambda: Vista.interfaz_principal(ventana) )
        archivoMenu.add_command(label="Consultar",command=lambda: Vista.interfaz_consultar(ventana) )
        archivoMenu.add_command(label="Cambiar",command=lambda: Vista.interfaz_buscar_id(ventana))
        archivoMenu.add_command(label="Borrar",command=lambda: Vista.interfaz_eliminar(ventana) )
        archivoMenu.add_separator()
        archivoMenu.add_command(label="Salir",command=ventana.quit)

    @staticmethod
    def interfaz_eliminar(ventana):
        Vista.limpiar_ventana(ventana)
        lbl_titulo = Label(ventana,text=".::Borrar una operacion::.", bg="#ffffff")
        lbl_titulo.pack(pady=10)
        lbl_id = Label(ventana,text="ID de la Operación:", bg="#ffffff")
        lbl_id.pack()
        id_var = IntVar()
        txt_id = Entry(ventana,textvariable=id_var) 
        txt_id.pack()
        # Uso de Funciones.respuesta centralizada en el método eliminar
        btn_eliminar = Button(ventana,text="Eliminar",command=lambda:Vista.eliminar(id_var.get()))
        btn_eliminar.pack(pady=10)
        btn_volver = Button(ventana,text="Volver",command=lambda:Vista.interfaz_principal(ventana))
        btn_volver.pack()
    
    @staticmethod
    def interfaz_consulta(ventana):
        Vista.limpiar_ventana(ventana)
        Label(ventana,text="..::Listado de las Operaciones::..", bg="#ffffff").pack()
        consulta = Operaciones.consultar()
        
        if consulta:
            frame_operaciones = Frame(ventana)
            frame_operaciones.pack(fill="both", expand=True, padx=20, pady=10)
        else:
            messagebox.showinfo(icon="info", message="No existen operaciones guardadas en la Base de Datos")

        for i, fila in enumerate(consulta):
            fecha = fila[1]

            labelDatos = f"Operacion: {i+1} ID: {fila[0]} Fecha de Creación: {fecha}\n" \
                f"Operación: {fila[2]}{fila[4]}{fila[3]}={fila[5]:.2f}"
            labelResultado=Label(frame_operaciones,text=labelDatos)
            labelResultado.pack(fill="x", pady=5) 
        btn_volver = Button(ventana,text="Volver",command=lambda:Vista.interfaz_principal(ventana))
        btn_volver.pack()
    
    @staticmethod
    def interfaz_consultar(ventana):
        Vista.limpiar_ventana(ventana)
        Label(ventana,text="..::Listado de las Operaciones::..", bg="#ffffff").pack()
        consulta = Operaciones.consultar()
        columnas = ["ID","Fecha","Num 1", "Num 2","Signo","Resultado"]
        tamaños = [30,70,40,40,30,50]
        tabla = ttk.Treeview(ventana, columns=columnas, show="headings")
        i = 0
        for col in columnas:
            tabla.heading(col, text=col)
            tabla.column(col, anchor="center", width=tamaños[i])
            i+=1
        for fila in consulta:
            tabla.insert("", "end", values=fila)
        tabla.pack(fill="both", expand=True)
        def seleccionar_fila(event):
            fila = tabla.selection()  # Obtiene ID(s) de las filas seleccionadas
            if fila:
                valores = tabla.item(fila[0], "values")  # Obtiene los valores
        tabla.bind("<<TreeviewSelect>>", seleccionar_fila)
        """ btn_calcular = Button(ventana,text="=",font=("Arial",14),command="",width=10)
        btn_calcular.pack() """
        """ 
        btn_eliminar = Button(ventana,text="Eliminar",font=("Arial",14),command=lambda:funciones.Funciones.eliminar(self.valores[0]),width=10)
        btn_eliminar.pack(pady=10)
        """

        btn_salir = Button(ventana,text="Salir",font=("Arial",14),command=ventana.destroy,width=10)
        btn_salir.pack(pady=10)
    
    @staticmethod
    def interfaz_buscar_id(ventana):
        Vista.limpiar_ventana(ventana)
        Vista.menuPrincipal(ventana)
        
        Label(ventana, text="Paso 1: Buscar Operación", font=("Arial", 14, "bold")).pack(pady=20)
        Label(ventana, text="Escribe el ID de la operación:").pack()
        
        var_id_buscar = IntVar()
        entry_buscar = Entry(ventana, textvariable=var_id_buscar)
        entry_buscar.pack(pady=5)
        entry_buscar.focus() 

        def verificar_existencia():
            id_buscado = var_id_buscar.get()
            lista_operaciones = Operaciones.consultar()
            
            encontrado = False
            
            for fila in lista_operaciones:
                if str(fila[0]) == str(id_buscado):
                    encontrado = True
                    Vista.interfaz_cambiar(ventana, fila[0], fila[2], fila[3], fila[4], fila[5])
                    break 
            
            if not encontrado:
                messagebox.showerror("Error", "Ese ID no existe en la base de datos")

        Button(ventana, text="Buscar", command=verificar_existencia, bg="#dddddd").pack(pady=10)
        # Permite pulsar "Enter" para buscar
        ventana.bind('<Return>', lambda event: verificar_existencia())
    

    @staticmethod
    def interfaz_cambiar(ventana, id_encontrado, num1_encontrado, num2_encontrado, signo_encontrado, resultado_encontrado):
        Vista.limpiar_ventana(ventana)
        Vista.menuPrincipal(ventana)
        # Títulos
        Label(ventana, text="Calculadora Básica", font=("Arial", 18, "bold")).pack(pady=10)
        Label(ventana, text=".:: Modificar Datos ::.", font=("Arial", 14)).pack(pady=10)
        
        frame_campos = Frame(ventana, bg="white") 
        frame_campos.pack(padx=50, pady=20)

        # Campo ID 
        
        Label(frame_campos, text="ID de la Operación:" , bg="white").grid(row=0, column=0, pady=10, sticky="w")
        id_operacion = IntVar(value=0) 
        id_operacion.set(id_encontrado)
        txt_id = Entry(frame_campos, textvariable=id_operacion, width=20, state="readonly")
        txt_id.grid(row=0, column=1)

        Label(frame_campos, text="Nuevo numero 1:").grid(row=1, column=0)
        var_n1 = IntVar()
        var_n1.set(num1_encontrado)
        Entry(frame_campos, textvariable=var_n1).grid(row=1, column=1)
        
        Label(frame_campos, text="Nuevo numero 2: ").grid(row=2, column=0)
        var_n2 = IntVar()
        var_n2.set(num2_encontrado)
        Entry(frame_campos, textvariable=var_n2).grid(row=2, column=1)
        
        Label(frame_campos, text="Nuevo Signo:").grid(row=3, column=0)
        var_sig = StringVar()
        var_sig.set(signo_encontrado) 
        Entry(frame_campos, textvariable=var_sig).grid(row=3, column=1)
        
        Label(frame_campos, text="Nuevo Resultado:").grid(row=4, column=0)
        var_res = StringVar()
        var_res.set(resultado_encontrado) 
        Entry(frame_campos, textvariable=var_res).grid(row=4, column=1)
        
        btn_guardar = Button(ventana, text="Guardar Cambios", 
                                command=lambda: Vista.cambiar(txt_id.get(), var_n1.get(), var_n2.get(), var_sig.get(), 0))
        btn_guardar.pack(pady=20)

        Button(ventana, text="Cancelar", command=lambda: Vista.interfaz_principal(ventana)).pack()
        
        # # Nuevo Número 1
        # Label(frame_campos, text="Nuevo Número 1: ",  bg="white").grid(row=1, column=0, pady=10, sticky="w")
        # valor1 = IntVar()
        # txt_val1 = Entry(frame_campos, textvariable=valor1, width=20)
        # txt_val1.grid(row=1, column=1)

        # # Nuevo Número 2
        # Label(frame_campos, text="Nuevo Número 2:",  bg="white").grid(row=2, column=0, pady=10, sticky="w")
        # valor2 = IntVar()
        # txt_val2 = Entry(frame_campos, textvariable=valor2, width=20)
        # txt_val2.grid(row=2, column=1)

        # # Nuevo Signo
        # Label(frame_campos, text="Nuevo Signo:",  bg="white").grid(row=3, column=0, pady=10, sticky="w")
        # signo = StringVar()
        # txt_signo = Entry(frame_campos, textvariable=signo, width=20)
        # txt_signo.grid(row=3, column=1)

        # # Nuevo Resultado
        # Label(frame_campos, text="Nuevo Resultado:",  bg="white").grid(row=4, column=0, pady=10, sticky="w")
        # resultado = DoubleVar()
        # txt_resultado = Entry(frame_campos, textvariable=resultado, width=20)
        # txt_resultado.grid(row=4, column=1)

        # Botones
        frame_botones = Frame(ventana)
        frame_botones.pack(pady=30)

        # btn_guardar = Button(frame_botones, text="Guardar", command=lambda: Vista.cambiar( id_operacion.get(),
        #         valor1.get(),
        #         valor2.get(),
        #         signo.get(),
        #         resultado.get() 
        #     ),
        #     width=15
        # )
        # btn_guardar.pack(pady=5) 

        btn_volver = Button(
            frame_botones,
            text="Volver",
            command=lambda: Vista.interfaz_principal(ventana),
            width=15
        )
        btn_volver.pack(pady=5)
    
    #------------------------------------------------------------------------------------
    #       Metodo para borrar pantalla
    #------------------------------------------------------------------------------------
    @staticmethod
    def limpiar_ventana(ventana):
        for widget in ventana.winfo_children():
            # widget.destroy()
            widget.pack_forget()

    @staticmethod
    def eliminar(id_op):
        """Intenta eliminar y usa la respuesta centralizada del controlador."""
        # Se verifica que el ID no sea 0 o vacío
        if not id_op or id_op == 0:
            messagebox.showerror("Error de ID", "Debe ingresar un ID válido para eliminar.")
            return

        eliminado = Operaciones.eliminar(id_op)
        # Uso de Funciones.respuesta
        Funciones.respuesta(eliminado, accion=f"La eliminación del registro con ID:{id_op}")
        
    # @staticmethod
    # def eliminar(id):
    #     eliminar = Operaciones.eliminar(id)
    #     if eliminar:
    #         messagebox.showinfo("Exito",f"Se eliminó el registro con ID:{id} exitosamente")
    #     else:
    #         messagebox.showinfo("Error",f"No fue posible eliminar el registro")
    
    
    @staticmethod
    def cambiar(id_op, val1, val2, signo, nuevo_resultado_manual):
        """Calcula el resultado automáticamente y actualiza el registro."""
        resultado_calculado = None
        try:
            # 1. Validación y Cálculo
            if signo == '+':
                resultado_calculado = val1 + val2
            elif signo == '-':
                resultado_calculado = val1 - val2
            elif signo == 'x' or signo == '*':
                resultado_calculado = val1 * val2
            elif signo == '/':
                if val2 == 0:
                    raise ZeroDivisionError("División por cero")
                resultado_calculado = val1 / val2
            else:
                messagebox.showerror("Error", "Signo de operación no válido. Use +, -, x, /")
                return
        except Exception as e:
            messagebox.showerror("Error de Cálculo", f"Verifique los valores ingresados: {e}")
            return
        
        actualizado = Operaciones.actualizar(val1, val2, signo, resultado_calculado, id_op)    
        
        Funciones.respuesta(actualizado, accion=f"La actualización del registro con ID:{id_op}")

    # @staticmethod
    # def cambiar(id_op, val1, val2, signo, nuevo_resultado_manual):
    #     resultado_calculado = None
    #     if signo == '+':
    #         resultado_calculado = val1 + val2
    #     elif signo == '-':
    #         resultado_calculado = val1 - val2
    #     elif signo == 'x':
    #         resultado_calculado = val1 * val2
    #     elif signo == '/':
    #         resultado_calculado = val1 / val2
    #     else:
    #         messagebox.showerror("Error", "Signo de operación no válido. Use +, -, *, /")
    #         return

    #     actualizado = Operaciones.actualizar(val1, val2,signo,resultado_calculado, id_op)         
    #     if actualizado:
    #         messagebox.showinfo("Éxito", f"El registro con ID:{id_op} fue actualizado exitosamente")
    #     else:
    #         messagebox.showerror("Desacierto con el ID", f"No fue posible actualizar el registro con ID:{id_op}. Verifique el ID.")

    @staticmethod
    def interfaz_principal(ventana):
        Vista.menuPrincipal(ventana)
        Vista.limpiar_ventana(ventana)
        Label(ventana,text="CALCULADORA",font=("Arial",20,"bold"),  bg="white").pack()
        frame_valores = Frame(ventana,  bg="white")
        frame_valores.pack(fill="x",padx=100)
        lbl_val1 = Label(frame_valores,text="Valor 1",font=("Arial",16),  bg="white")
        lbl_val1.grid(row=0,column=0)
        valor1 = IntVar()
        entry1 = Entry(frame_valores,width=10,textvariable=valor1,  bg="white")
        entry1.grid(row=0,column=1)

        lbl_val1 = Label(frame_valores,text="Valor 2",font=("Arial",16),  bg="white")
        lbl_val1.grid(row=1,column=0)
        valor2 = IntVar()
        entry2 = Entry(frame_valores,width=10,textvariable=valor2,  bg="white")
        entry2.grid(row=1,column=1)

        frame_botones = Frame(ventana,  bg="white")
        frame_botones.pack(fill="x",padx=70,pady=20)

        btn_suma = Button(frame_botones,text="+",font=("Arial",14),command=lambda: Funciones.operaciones(valor1.get(), valor2.get(), signo="+"),width=10)
        btn_suma.grid(row=0,column=0,padx=5,pady=5)

        btn_resta = Button(frame_botones,text="-",font=("Arial",14),command=lambda: Funciones.operaciones(valor1.get(), valor2.get(), signo="-"),width=10)
        btn_resta.grid(row=0,column=1,padx=5,pady=5)

        btn_multi = Button(frame_botones,text="x",font=("Arial",14),command=lambda: Funciones.operaciones(valor1.get(), valor2.get(), signo="x"),width=10)
        btn_multi.grid(row=0,column=2,padx=5,pady=5)

        btn_div = Button(frame_botones,text="/",font=("Arial",14),command=lambda: Funciones.operaciones(valor1.get(), valor2.get(), signo="/"),width=10)
        btn_div.grid(row=0,column=3,padx=5,pady=5)
        
        btn_salir = Button(ventana,text="Salir",font=("Arial",14),command=ventana.destroy,width=10)
        btn_salir.pack(pady=10)
        
        
        
        
        
        # else:
        #     Label(ventana, text="No hay operaciones registradas.", font=("Arial", 12)).pack(pady=20)
        
        # Label(ventana,text="Historial").pack()
        # consulta = Operaciones.consultar()
        # columnas = ["ID","Fecha","Num 1", "Num 2","Signo","Resultado"]
        # tamaños = [30,70,40,40,30,50]
        # tabla = ttk.Treeview(ventana, columns=columnas, show="headings")
        # i = 0
        # for col in columnas:
        #     tabla.heading(col, text=col)
        #     tabla.column(col, anchor="center", width=tamaños[i])
        #     i+=1
        # for fila in consulta:
        #     tabla.insert("", "end", values=fila)
        # tabla.pack(fill="both", expand=True)
        # def seleccionar_fila(event):
        #     fila = tabla.selection()  # Obtiene ID(s) de las filas seleccionadas
        #     if fila:
        #         self.valores = tabla.item(fila[0], "values")  # Obtiene los valores
        # tabla.bind("<<TreeviewSelect>>", seleccionar_fila)
        # """ btn_calcular = Button(ventana,text="=",font=("Arial",14),command="",width=10)
        # btn_calcular.pack() """
        # """ 
        # btn_eliminar = Button(ventana,text="Eliminar",font=("Arial",14),command=lambda:funciones.Funciones.eliminar(self.valores[0]),width=10)
        # btn_eliminar.pack(pady=10)
        # """


# class Vista:
#     def __init__(self, ventana):
#         self.ventana=ventana
#         ventana.title("Calculadora")
#         ventana.geometry("800x600")
#         ventana.resizable(False, False)
        
#         # --- 1. Marcos contenedores ---
#         self.frame_principal = Frame(self.ventana) # Frame para la calculadora
#         self.frame_eliminar = Frame(self.ventana) # Frame para el menú borrar
        
#         # --- 2. Construir la interfaz principal ---
#         # Llamamos a tu función. Esta función AHORA usará self.frame_principal
#         self.interfazPrincipal() # <-- CAMBIO: Ya no le pasamos 'ventana'
        
#         # --- 3. Construir el menú (estático) ---
#         # Le pasamos 'self' (la instancia) para que pueda controlar los frames
#         Vista.menuPrincipal(self.ventana, self) 
            
#         # 4. Mostrar la interfaz principal al inicio
#         self.frame_principal.pack(fill="both", expand=True)
#     def interfazPrincipal(self):
#         n1=IntVar()
#         n2=IntVar()

#         txt_valor1=Entry(self.frame_principal, textvariable=n1, width=5, justify=RIGHT) 
#         txt_valor1.pack()

#         txt_valor2=Entry(self.frame_principal, textvariable=n2, width=5, justify=RIGHT) 
#         txt_valor2.pack()

#         marco_principal=Frame(self.frame_principal, width=800, height=300) 
#         marco_principal.pack()

#         btn_sumar=Button(marco_principal, text="Sumar", command=lambda: Funciones.operaciones(n1.get(), n2.get(), signo="+"))
#         btn_sumar.grid(row=0, column=0, pady=5, padx=5,)

#         btn_restar=Button(marco_principal, text="Restar", command=lambda: Funciones.operaciones(n1.get(), n2.get(), signo="-"))
#         btn_restar.grid(row=0, column=1, pady=5, padx=5,)

#         btn_multiplicar=Button(marco_principal, text="Multiplicar", command=lambda: Funciones.operaciones(n1.get(), n2.get(), signo="x"))
#         btn_multiplicar.grid(row=0, column=3, pady=5, padx=5,)

#         btn_dividir=Button(marco_principal, text="Dividir", command=lambda: Funciones.operaciones(n1.get(), n2.get(), signo="/"))
#         btn_dividir.grid(row=0, column=4, pady=5, padx=5,)

#         btn_salir=Button(marco_principal, text="Salir", command=self.ventana.quit)
#         btn_salir.grid(row=1, column=2, pady=5, padx=5,)
        
#     @staticmethod
#     def menuPrincipal(ventana, vista_instance):
#         menuBar=Menu(ventana)
#         ventana.config(menu=menuBar)

#         operacionesMenu= Menu(menuBar, tearoff=False)
#         menuBar.add_cascade(label="Operaciones", menu=operacionesMenu)
#         operacionesMenu.add_command(label="Agregar", command=lambda: "")
#         operacionesMenu.add_command(label="Consultar", command=lambda: "")
#         operacionesMenu.add_command(label="Cambiar",  command=lambda: "")
#         operacionesMenu.add_command(label="Borrar", command=lambda: Vista.eliminar(vista_instance))
#         operacionesMenu.add_separator()
#         operacionesMenu.add_command(label="Salir", command=ventana.quit)
        
#     @staticmethod
#     def eliminar(vista_instance):
#         vista_instance.frame_principal.pack_forget() # <-- CAMBIO
        
#         # 2. Limpiamos el frame_eliminar (por si se presiona varias veces)
#         for widget in vista_instance.frame_eliminar.winfo_children():
#             widget.destroy()
#         marcoEliminar = Frame(vista_instance.frame_eliminar, width=800, height=300)
#         marcoEliminar.pack(pady=20)

#         lbl_nombre=Label(marcoEliminar, text="..:: Borrar una Operacion::.. ")
#         lbl_nombre.pack(pady=5)
        
#         frame_input = Frame(marcoEliminar)
#         frame_input.pack(pady=10)
        
#         lbl_ope=Label(frame_input, text="ID de la operacion")
#         lbl_ope.pack(side=LEFT, padx=5)
        
#         ideOpe=Entry(frame_input)
#         ideOpe.pack(side=LEFT)
        
#         btn_eliminar=Button(marcoEliminar, text="Eliminar")
#         btn_eliminar.pack(pady=5)
        
#         btn_volver=Button(marcoEliminar, text="Volver", 
#             command=lambda: Vista.mostrar_principal(vista_instance))
#         btn_volver.pack(pady=5)
        
#         vista_instance.frame_eliminar.pack(fill="both", expand=True)
    
    # @staticmethod
    # def mostrar_principal(vista_instance): 
    #     """Oculta el frame de eliminar y vuelve a mostrar el principal"""
    #     vista_instance.frame_eliminar.pack_forget()
    #     vista_instance.frame_principal.pack(fill="both", expand=True)
        
    
    
    ''' 
def suma(n1, n2):
    sumar=n1+n2
    messagebox.showinfo(title="Suma", message=f"{n1}+{n2} = {sumar}", icon="info")

def resta(n1, n2):
    restar=n1-n2
    messagebox.showinfo(title="Resta", message=f"{n1}-{n2} = {restar}", icon="info")

def multiplicar(n1, n2):
    multiplicacion=n1*n2
    messagebox.showinfo(title="Multiplicacion", message=f"{n1}*{n2} = {multiplicacion}", icon="info")


def division(n1, n2):
    divisar=n1/n2
    messagebox.showinfo(title="Division", message=f"{n1}/{n2} = {divisar}", icon="info")

'''
    