class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas=llantas
        self._color=color
        self._precio=precio
        
class Moto(Fabrica):
    def Mostrar_moto(self):
        print("---CARACTERISTICAS MOTO---")
        print(f"Cantidad de llantas: ", {self._llantas})
        print(f"Cantidad de color: ", {self._color})
        print(f"Cantidad de precio: ", {self._precio})
        
class Carro(Fabrica):
    def Mostrar_Carro(self):
        print("---CARACTERISTICAS CARRO---")
        print(f"cantidad de llantas: ", {self._llantas})
        print(f"cantidad de color: ", {self._color})
        print(f"cantidad de precio: ", {self._precio})
        
motoFab=Moto(2, "roja", 100)
CarroFab=Carro(4, "roja", 1000)

motoFab.Mostrar_moto()
CarroFab.Mostrar_Carro()