'''
Crear una calculadora: 
1.- Dos campos de texto
2.- 4 Botones para las Operaciones
3.- Mostrar el resultado
'''

from tkinter import *
from tkinter import messagebox

# def mensaje(n1, n2, ope, signo, tipo_ope):
#     messagebox.showinfo(title=tipo_ope, icon="info", message=f"{n1}{signo}{n2}*{ope}")

# def suma(n1, n2):
#     ope=n1+n2
#     mensaje=(n1, n2, ope, "+", "Suma")
    
# def resta(n1, n2):
#     ope=n1+n2
#     mensaje=(n1, n2, ope, "+", "Resta")
    
# def multiplicacion(n1, n2):
#     ope=n1+n2
#     mensaje=(n1, n2, ope, "+", "Multiplicacion")
    
# def division(n1, n2):
#     ope=n1+n2
#     mensaje=(n1, n2, ope, "+", "Division")

def mostrar_resultado(titulo, mensaje):
    messagebox.showinfo(title=titulo, message=mensaje, icon="info")

def borrar():
    ventana.quit()
    
def suma(n1, n2):
    mostrar_resultado(titulo="Suma", 
                    mensaje=f"{n1} + {n2} = {n1 + n2}")

def resta(n1, n2):
    mostrar_resultado(titulo="Resta", 
                    mensaje=f"{n1} - {n2} = {n1 - n2}")

def multiplicar(n1, n2):
    mostrar_resultado(titulo="Multiplicación", 
                    mensaje=f"{n1} * {n2} = {n1 * n2}")

def division(n1, n2):
        mostrar_resultado(titulo="División", 
                        mensaje=f"{n1} / {n2} = {n1 / n2}")


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

btn_sumar=Button(marco_principal, text="Sumar", command=lambda: suma(n1.get(), n2.get()))
btn_sumar.grid(row=0, column=0, pady=5, padx=5,)

btn_restar=Button(marco_principal, text="Restar", command=lambda: resta(n1.get(), n2.get()))
btn_restar.grid(row=0, column=1, pady=5, padx=5,)

btn_multiplicar=Button(marco_principal, text="Multiplicar", command=lambda: multiplicar(n1.get(), n2.get()))
btn_multiplicar.grid(row=0, column=2, pady=5, padx=5,)

btn_dividir=Button(marco_principal, text="Dividir", command=lambda: division(n1.get(), n2.get()))
btn_dividir.grid(row=0, column=3, pady=5, padx=5,)

btn_dividir=Button(marco_principal, text="Salir", command=borrar, width=10, font=("Arial", 10, "bold"))
btn_dividir.grid(row=2, column=2, pady=3, padx=3)


resultado=Label(ventana, text="")
resultado.pack()


ventana.mainloop()