from django.shortcuts import render

# Create your views here.
def vista_ventas(request):
    return render(request,'ventas.html')