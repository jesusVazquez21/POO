#DOCUMENTACION INTERNA

class Coche:
    """
    Clase que representa un coche.
    Atributos:
        marca (str): Marca del coche.
        modelo (str): Modelo del coche.
        velocidad (int): Velocidad actual del coche.
    """

    def __init__(self, marca, modelo):
        """Inicializa el coche con una marca y modelo."""
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0

    def acelerar(self, cantidad):
        """Aumenta la velocidad del coche en la cantidad indicada."""
        self.velocidad += cantidad



