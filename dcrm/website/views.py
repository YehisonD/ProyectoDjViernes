from django.shortcuts import redirect, render
# pyrefly: ignore [missing-import]
from .models import Record
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib import messages
# pyrefly: ignore [missing-import]
from .forms import UserRegisterForm, RecordForm

def home(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password= password)
        if user is not None:
            login(request, user)
            messages.success(request,"ingresado exitosamente")
            return redirect('home')
        else:
            messages.error(request," las credenciales son invalidas !!📢")
            return render(request, 'home.html', {})
    else:
        records = Record.objects.all()
        is_admin = request.user.is_authenticated and (request.user.groups.filter(name='Administrador').exists() or request.user.is_superuser)
        return render(request, 'home.html', {'records': records, 'is_admin': is_admin})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request,"cerraste la session correctamente")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            group, created = Group.objects.get_or_create(name='Usuario')
            user.groups.add(group)
            
            Record.objects.create(
                first_name=form.cleaned_data.get('first_name', ''),
                last_name=form.cleaned_data.get('last_name', ''),
                email=form.cleaned_data.get('email', ''),
                phone_number=form.cleaned_data.get('phone', ''),
                address=form.cleaned_data.get('address', ''),
                city=form.cleaned_data.get('city', ''),
                state=form.cleaned_data.get('state', ''),
                zip_code=form.cleaned_data.get('zip_code', '')
            )
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request,"registro exitoso")
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html',{'form': form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        is_admin = request.user.groups.filter(name='Administrador').exists() or request.user.is_superuser
        return render(request, 'record.html', {'customer_record': customer_record, 'is_admin': is_admin})
    else:
        messages.error(request,"debes iniciar sesion para ver el registro del cliente")
        return redirect('home')

def delete_record(request, pk):
    if request.user.is_authenticated:
        if not request.user.groups.filter(name='Administrador').exists() and not request.user.is_superuser:
            messages.error(request, "No tienes permisos de Administrador para eliminar registros.")
            return redirect('home')
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request,"registro eliminado correctamente")
        return redirect('home')
    else:
        messages.error(request,"debes iniciar sesion para eliminar el registro del cliente")
        return redirect('home')

def update_record(request, pk):
    if request.user.is_authenticated:
        if not request.user.groups.filter(name='Administrador').exists() and not request.user.is_superuser:
            messages.error(request, "No tienes permisos de Administrador para actualizar registros.")
            return redirect('home')
        current_record = Record.objects.get(id=pk)
        form = RecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request,"registro actualizado correctamente")
            return redirect('home')
        return render(request, 'update_record.html', {'form': form, 'customer_record': current_record})
    else:
        messages.error(request,"debes iniciar sesion para actualizar el registro del cliente")
        return redirect('home')

def add_record(request):
    form = RecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "Registro añadido correctamente")
                return redirect('home')
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.error(request, "Debes iniciar sesión para añadir un registro")
        return redirect('home')
