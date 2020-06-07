from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import json
import datetime
from .models import *
from django_tables2 import SingleTableView
from .tables import ProfileTable
from .forms import  ProfileForm, CustomUserForm, ClientForm, ProductoForm, SellerForm, EmployeeForm, SupplierForm
from .utils import cookieCart, cartData, guestOrder
import django_tables2 as tables


#Borrar esta vista
class TableView(tables.SingleTableView):
    table_class = ProfileTable
    queryset = Profile.objects.all()
    template_name = 'admin/users.html'
#Borrar
def users(request):
    users = Profile.objects.all()
    table = ProfileTable( users )
    context = {'table': table}
    return render(request, 'admin/users.html', context)
#Listado Usuarios        
def listUser(request):
    users = Profile.objects.all()
    data={
        'users': users
    }
    return render(request, 'admin/listado_usuarios.html', data)
#Eliminar usuario desde tabla
def deleteUser(request, pk):
    user = User.objects.get(pk=pk)
    perfil = Profile.objects.get(user_id=pk)
    user.delete()
    profile.delete()
    return redirect(to='store')
#Editar usuario desde tabla
def editUser(request, pk):
    usuario = User.objects.get(pk=pk)
    perfil = Profile.objects.get(user_id=pk)
    data = {
        'form': CustomUserForm(instance=usuario),
        'profile': ProfileForm(instance=perfil)
    }
    if request.method == 'POST':
        formulario = CustomUserForm(data=request.POST, instance=usuario)
        profile = ProfileForm(data=request.POST, instance=perfil)
        if formulario.is_valid():
            formulario.save()
            profile.save()
            data['mensaje']='Usuario modificado correctamente'
            login(request, usuario)
            return redirect(to='store')
        data['form']=CustomUserForm(instance=User.objects.get(pk=pk))
        data['profile']=ProfileForm(instance=perfil)
    return render(request,'admin/edit_user.html', data)
#Registrar Cliente
def registerClient(request):
    data = {
       'form': CustomUserForm(),
        'profile': ProfileForm(),
        'client': ClientForm()
    }
    if request.method=='POST':
        form = CustomUserForm(request.POST)
        profile = ProfileForm(request.POST)
        client = ClientForm(request.POST)
        if form.is_valid() and profile.is_valid():
            new_user = form.save()
            profile = profile.save(commit=False)
            profile.user = new_user
            profile.save()
            client = client.save(commit=False)
            client.profile = profile
            client.save() 
            #autenticar el usuario y redirigirlo
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            #autentificamos credenciales del usuario
            user = authenticate(username=username, password=password)
            return redirect(to='store')
        data['form']=form
        data['profile']=profile
    return render(request, 'accounts/register_client.html', data)
#Registrar Vendedor
def registerSeller(request):
    data = {
       'form': CustomUserForm(),
        'profile': ProfileForm(),
        'seller': SellerForm()
    }
    if request.method=='POST':
        form = CustomUserForm(request.POST)
        profile = ProfileForm(request.POST)
        seller = SellerForm(request.POST)
        if form.is_valid() and profile.is_valid():
            new_user = form.save()
            profile = profile.save(commit=False)
            profile.user = new_user
            profile.save()
            #if client.is_valid():
            seller = seller.save(commit=False)
            seller.profile = profile
            seller.save() 
            #autenticar el usuario y redirigirlo
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            #autentificamos credenciales del usuario
            user = authenticate(username=username, password=password)
            return redirect(to='store')
        data['form']=form
        data['profile']=profile
    return render(request, 'accounts/register_seller.html', data)
#Registrar Proveedor
def registerSupplier(request):
    data = {
       'form': CustomUserForm(),
        'profile': ProfileForm(),
        'supplier': SupplierForm()
    }
    if request.method=='POST':
        form = CustomUserForm(request.POST)
        profile = ProfileForm(request.POST)
        supplier = SupplierForm(request.POST)
        if form.is_valid() and profile.is_valid():
            new_user = form.save()
            profile = profile.save(commit=False)
            profile.user = new_user
            profile.save()
            #if client.is_valid():
            supplier = supplier.save(commit=False)
            supplier.profile = profile
            supplier.save() 
            #autenticar el usuario y redirigirlo
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            #autentificamos credenciales del usuario
            user = authenticate(username=username, password=password)
            return redirect(to='store')
        data['form']=form
        data['profile']=profile
    return render(request, 'accounts/register_supplier.html', data)
#Registrar Empleado
def registerEmployee(request):
    data = {
       'form': CustomUserForm(),
        'profile': ProfileForm(),
        'employee': EmployeeForm()
    }
    if request.method=='POST':
        form = CustomUserForm(request.POST)
        profile = ProfileForm(request.POST)
        employee = EmployeeForm(request.POST)
        if form.is_valid() and profile.is_valid():
            new_user = form.save()
            profile = profile.save(commit=False)
            profile.user = new_user
            profile.save()
            #if client.is_valid():
            employee = employee.save(commit=False)
            employee.profile = profile
            employee.save() 
            #autenticar el usuario y redirigirlo
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            #autentificamos credenciales del usuario
            user = authenticate(username=username, password=password)
            return redirect(to='store')
        data['form']=form
        data['profile']=profile
    return render(request, 'accounts/register_employee.html', data)

def editLoggedUser(request, pk):
    usuario = User.objects.get(pk=pk)
    perfil = request.user.profile
    data = {
        'form': CustomUserForm(instance=usuario),
        'profile': ProfileForm(instance=perfil)
    }
    if request.method == 'POST':
        formulario = CustomUserForm(data=request.POST, instance=usuario)
        profile = ProfileForm(data=request.POST, instance=perfil)
        if formulario.is_valid():
            formulario.save()
            profile.save()
            data['mensaje']='Usuario modificado correctamente'
            login(request, usuario)
            return redirect(to='store')
        data['form']=CustomUserForm(instance=User.objects.get(pk=pk))
        data['profile']=ProfileForm(instance=perfil)
    return render(request,'admin/edit_user.html', data)
#Registro de usuario
def registerPage(request):
    data = {
       'form': CustomUserForm(),
        'profile': ProfileForm(),
        'client': ClientForm()
    }
    if request.method=='POST':
        form = CustomUserForm(request.POST)
        profile = ProfileForm(request.POST)
        client = ClientForm(request.POST)
        if form.is_valid() and profile.is_valid():
            new_user = form.save()
            profile = profile.save(commit=False)
            profile.user = new_user
            profile.save()
            #if client.is_valid():
            client = client.save(commit=False)
            client.profile = profile
            client.save()
            #autenticar el usuario y redirigirlo
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            #autentificamos credenciales del usuario
            user = authenticate(username=username, password=password)
            #logueamos el usuario
            login(request, user)
            return redirect(to='store')
        data['form']=form
        data['profile']=profile
    return render(request, 'accounts/register.html', data)

def editPage(request, id):
    usuario = User.objects.get(id=id)
    perfil = request.user.profile
    data = {
        'form': CustomUserForm(instance=usuario),
        'profile': ProfileForm(instance=perfil)
    }
    if request.method == 'POST':
        formulario = CustomUserForm(data=request.POST, instance=usuario)
        profile = ProfileForm(data=request.POST, instance=perfil)
        if formulario.is_valid():
            formulario.save()
            profile.save()
            data['mensaje']='Usuario modificado correctamente'
            login(request, usuario)
            return redirect(to='store')
        data['form']=CustomUserForm(instance=User.objects.get(id=id))
        data['profile']=ProfileForm(instance=perfil)
    return render(request,'accounts/edit.html', data)

def deletePage(request):
    user = request.user
    user.delete()
    return redirect(to='store')

    return render(request, 'accounts/delete.html', data)

#Log In
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('')
        else:
            messages.info('Usuario o Contraseña incorrectos')
    context= {}
    return render(request, 'accounts/login.html', context)
#Log Out
def logoutUser(request):
    logout(request)
    return redirect('')
#Pagina Principal
def store(request):

    data = cartData(request)
    cartItems = data['cartItems']

    products = Producto.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/store.html', context)
#Carrito de Compra
def cart(request):

    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)
#Check Out
def checkout(request):

    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems': cartItems}
    return render(request, 'store/checkout.html', context)
#Actualizar productos del carro
def updateItems(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    usuario = request.user.profile
    product = Producto.objects.get(id=productId)
    order, created = Order.objects.get_or_create(usuario=usuario, complete=False)

    orderItems, created = OrderItems.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItems.quantity = (orderItems.quantity + 1)
    elif action == 'remove':
        orderItems.quantity = (orderItems.quantity - 1)

    orderItems.save()

    if orderItems.quantity <= 0:
        orderItems.delete()

    return JsonResponse('Producto agregado', safe=False)
#Generar Venta
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    total  = float(data['form']['total'])

    if request.user.is_authenticated:
        usuario = request.user.profile
        order, created = Order.objects.get_or_create(usuario=usuario, complete=False)
        if usuario.tipo == 'Vendedor':
            boleta = Boleta.objects.get_or_create(
            order=order,
            n_boleta=transaction_id,
            total=total,
            vendedor = usuario.name
        )
        else:
            boleta = Boleta.objects.get_or_create(
            order=order,
            n_boleta=transaction_id,
            total=total,
            vendedor = 'Tienda Ferme'
        )
    else:
       usuario, order = guestOrder(request, data)
       boleta = Boleta.objects.get_or_create(
        order=order,
        n_boleta=transaction_id,
        total=total,
        vendedor = 'Tienda Ferme'
        )

    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            usuario=usuario,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
        )
    return JsonResponse('Pago realizado', safe=False)
#Administracion de Productos
def adm_productos(request):
    prods = Producto.objects.all()
    data={
        'prods': prods
    }
    return render(request, 'store/adm-producto.html', data)

def agregar_producto(request):
    data={
    'form': ProductoForm()
    }
    if request.method=='POST':
        formulario = ProductoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            #formulario = formulario.save(commit=False)
            #formulario.user = request.user
            formulario.save()
            data['mensaje']='Producto agregado con éxito'
        data['form']=formulario
    return render(request, 'store/agregar-producto.html', data)
