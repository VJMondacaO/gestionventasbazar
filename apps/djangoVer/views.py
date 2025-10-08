from django.shortcuts import render
from .models import Productos, Clientes
from .form import ProductoRegistroForm, ClienteRegistroForm

# Redirigir a al sitio deseado
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    productos_destacados = Productos.objects.filter(estado='disponible')[:6]
    total_productos = Productos.objects.count()
    total_clientes = Clientes.objects.count()
    
    data = {
        'productos_destacados': productos_destacados,
        'total_productos': total_productos,
        'total_clientes': total_clientes
    }
    return render(request, 'djangoVer/index.html', data)

def productosData(request):
    productos = Productos.objects.all()
    data = {'productos':productos}
    return render (request, 'djangoVer/productos.html', data)

def crearProducto(request):
    form = ProductoRegistroForm()
    
    if request.method == 'POST':
        form = ProductoRegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('productosData'))                  

    data = {'form' : form,
            'titulo' : 'Crear producto',
            'txtBoton' : 'Guardar producto'}
    return render(request, 'djangoVer/productoRegistro.html' ,data)

def editarProducto(request, id):
    producto = Productos.objects.get(id=id)
    form = ProductoRegistroForm(instance=producto)
    
    if request.method == 'POST':
        form = ProductoRegistroForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('productosData'))                  

    data = {'form' : form,
            'titulo' : 'Editar producto',
            'txtBoton' : 'Guardar cambios'}
    return render(request, 'djangoVer/productoRegistro.html' ,data)

def eliminarProducto(request, id):
    producto = Productos.objects.get(id=id)
    producto.delete()
    return HttpResponseRedirect(reverse('productosData'))

def clientesData(request):
    clientes = Clientes.objects.all()
    data = {'clientes':clientes}
    return render (request, 'djangoVer/clientes.html', data)

def crearCliente(request):
    form = ClienteRegistroForm()
    
    if request.method == 'POST':
        form = ClienteRegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('clientesData'))                  

    data = {'form' : form,
            'titulo' : 'Crear cliente',
            'txtBoton' : 'Guardar cliente'}
    return render(request, 'djangoVer/clienteRegistro.html' ,data)

def editarCliente(request, id):
    cliente = Clientes.objects.get(ID_Cliente=id)
    form = ClienteRegistroForm(instance=cliente)
    
    if request.method == 'POST':
        form = ClienteRegistroForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('clientesData'))                  

    data = {'form' : form,
            'titulo' : 'Editar cliente',
            'txtBoton' : 'Guardar cambios'}
    return render(request, 'djangoVer/clienteRegistro.html' ,data)

def eliminarCliente(request, id):
    cliente = Clientes.objects.get(ID_Cliente=id)
    cliente.delete()
    return HttpResponseRedirect(reverse('clientesData'))  