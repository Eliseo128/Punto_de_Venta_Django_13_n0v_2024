from django.urls import path
from ventas_app import views

urlpatterns = [
    path('',views.vista_ventas,name='vista_ventas')
]
