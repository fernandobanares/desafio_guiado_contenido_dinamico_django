from django.shortcuts import render

def hola(request):
    return render(request, 'hola.html', {})
def listaEmpleados(request):
    empleados = ['Fernando','Ana','Rigoberto','Muriel']
    context = {'empleados': empleados}
    return render (request, 'listaEmpleados.html', context)
