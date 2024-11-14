from django.urls import path
from clientes_app import views

urlpatterns = [
    path('',views.vista_clientes,name='vista_clientes')
]
