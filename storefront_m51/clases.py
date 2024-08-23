# storefront_m51/tu_app/clases.py
class Animal:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

    def descripcion(self):
        return f"{self.nombre} es un {self.especie}"

class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def descripcion(self):
        return f"{self.marca} {self.modelo} del año {self.año}"
