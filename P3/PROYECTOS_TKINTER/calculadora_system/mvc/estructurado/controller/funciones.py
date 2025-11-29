from tkinter import *
from tkinter import messagebox
    
    
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
    
    messagebox.showinfo(title=tipo_ope, icon="info", message=f"{n1}{signo}{n2} = {ope}")
        
    
    
    
# def suma(n1, n2):
#     sumar=n1+n2
#     messagebox.showinfo(title="Suma", message=f"{n1}+{n2} = {sumar}", icon="info")

# def resta(n1, n2):
#     restar=n1-n2
#     messagebox.showinfo(title="Resta", message=f"{n1}-{n2} = {restar}", icon="info")

# def multiplicar(n1, n2):
#     multiplicacion=n1*n2
#     messagebox.showinfo(title="Multiplicacion", message=f"{n1}*{n2} = {multiplicacion}", icon="info")


# def division(n1, n2):
#     divisar=n1/n2
#     messagebox.showinfo(title="Division", message=f"{n1}/{n2} = {divisar}", icon="info")