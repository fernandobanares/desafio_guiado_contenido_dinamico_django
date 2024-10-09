from django.urls import path
from ..nombres import views

urlpatterns = [
    path('empleados/', views.listaEmpleados, name='listaEmpleados'),
]
