class Fabrica:
    def __init__(self, llanta, color, precio):
        self._llanta=llanta
        self._color=color
        self._precio=precio
        
    @property
    def llanta(self):
        return self._llanta
    
    @llanta.setter
    def llanta(self, llanta):
        self._llanta=llanta
        
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        self._color=color
        
    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self, precio):
        self._precio=precio
        


class Moto(Fabrica):
    def __init__(self, llanta, color, precio, tipoMoto):
        Fabrica().__init__(llanta, color, precio)
        self._tipoMoto=tipoMoto
        
    @property
    def tipoMoto(self):
        return self._tipoMoto
    
    @tipoMoto.setter
    def tipoMoto(self, tipoMoto):
        self._tipoMoto=tipoMoto
        
class Carro(Fabrica):
        def __init__(self, llanta, color, precio, tipoCarro):
            Fabrica().__init__(llanta, color, precio)
            self._tipoCarro=tipoCarro
        @property
        def tipoCarro(self):
            return self._tipoCarro
    
        @tipoCarro.setter
        def tipoCarro(self, tipoCarro):
            self._tipoCarro=tipoCarro
        
moto1=Moto(2, "rojo", 1200, "sport")
carro1=Carro(4, "verde", 12000, "4x4")