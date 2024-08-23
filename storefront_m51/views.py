# storefront_m51/tu_app/views.py
from django.http import HttpResponse
from .clases import Animal, Vehiculo

def mostrar_animal(request):
    mi_animal = Animal(nombre="Toby", especie="Perro")
    descripcion = mi_animal.descripcion()
    return HttpResponse(f"Descripción del animal: {descripcion}")

def mostrar_vehiculo(request):
    mi_vehiculo = Vehiculo(marca="Toyota", modelo="Corolla", año=2021)
    descripcion = mi_vehiculo.descripcion()
    return HttpResponse(f"Descripción del vehículo: {descripcion}")
