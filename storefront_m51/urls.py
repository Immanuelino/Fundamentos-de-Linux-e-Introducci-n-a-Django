# storefront_m51/tu_app/urls.py
from django.urls import path
from .views import mostrar_animal, mostrar_vehiculo

urlpatterns = [
    path('animal/', mostrar_animal, name='mostrar_animal'),
    path('vehiculo/', mostrar_vehiculo, name='mostrar_vehiculo'),
]
