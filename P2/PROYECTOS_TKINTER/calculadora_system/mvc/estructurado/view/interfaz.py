'''
Crear una calculadora: 
1.- Dos campos de texto
2.- 4 Botones para las Operaciones
3.- Mostrar el resultado
'''

from tkinter import *
from tkinter import messagebox
from controller import funciones

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
def interfazPrincipal():
    def borrar():
        ventana.quit()

    ventana = Tk()
    ventana.title("Calculadora")
    ventana.geometry("800x600")
    ventana.resizable(False, False)


    n1=IntVar()
    n2=IntVar()

    txt_valor1=Entry(ventana, textvariable=n1, width=5, justify=RIGHT)
    txt_valor1.pack()

    txt_valor2=Entry(ventana, textvariable=n2, width=5, justify=RIGHT)
    txt_valor2.pack()

    marco_principal=Frame(ventana, width=800, height=300)
    marco_principal.pack()

    btn_sumar=Button(marco_principal, text="Sumar", command=lambda: funciones.operaciones(n1.get(), n2.get(), signo="+"))
    btn_sumar.grid(row=0, column=0, pady=5, padx=5,)

    btn_restar=Button(marco_principal, text="Restar", command=lambda: funciones.operaciones(n1.get(), n2.get(), signo="-"))
    btn_restar.grid(row=0, column=1, pady=5, padx=5,)

    btn_multiplicar=Button(marco_principal, text="Multiplicar", command=lambda: funciones.operaciones(n1.get(), n2.get(), signo="x"))
    btn_multiplicar.grid(row=0, column=3, pady=5, padx=5,)

    btn_dividir=Button(marco_principal, text="Dividir", command=lambda: funciones.operaciones(n1.get(), n2.get(), signo="/"))
    btn_dividir.grid(row=0, column=4, pady=5, padx=5,)

    btn_dividir=Button(marco_principal, text="Salir", command=borrar)
    btn_dividir.grid(row=1, column=2, pady=5, padx=5,)


    resultado=Label(ventana, text="")
    resultado.pack()


    ventana.mainloop()
    
    
    
    
    