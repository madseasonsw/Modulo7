from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import NewUserForm
from .models import Tarea
from .forms import TareaForm
from django.utils import timezone

def inicio(request):
    return render(request, 'inicio.html')

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("bienvenido") 
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

    form = NewUserForm()
    return render(request=request, template_name="Siete/register.html", context={"register_form":form})

def login_request(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/bienvenido")
        else:
            return render(request, "Siete/login.html", {"error": "Invalid username or password"})
    else:
        return render(request, "Siete/login.html")

def bienvenido(request):
    if request.user.is_authenticated:
        return render(request, "Siete/bienvenido.html")
    else:
        return redirect("Siete:login")
    

@login_required(login_url='login')  # Requiere inicio de sesión para acceder a la vista
def lista_tareas(request):
    tareas = Tarea.objects.filter(usuario=request.user, completada=False).order_by('fecha_vencimiento')
    return render(request, 'Siete/lista_tareas.html', {'tareas': tareas})

def ver_tarea(request, id_tarea):
    tarea = Tarea.objects.get(id=id_tarea)
    return render(request, 'Siete/ver_tarea.html', {'tarea': tarea})

def editar_tarea(request, id_tarea):
    tarea = Tarea.objects.get(id=id_tarea)

    if request.method == 'POST':
        tarea.nombre = request.POST['nombre']
        tarea.descripcion = request.POST['descripcion']
        # Asegúrate de actualizar cualquier otro campo que necesites
        tarea.save()
        return redirect('Siete:ver_tarea', id_tarea=tarea.id)

    return render(request, 'Siete/editar_tarea.html', {'tarea': tarea})

def eliminar_tarea(request, id_tarea):
    tarea = Tarea.objects.get(id=id_tarea)
    tarea.delete()
    return redirect('Siete:lista_tareas')

def completar_tarea(request, id_tarea):
    tarea = Tarea.objects.get(id=id_tarea)
    tarea.completada = True
    tarea.save()
    return redirect('Siete:ver_tarea', id_tarea=tarea.id)

@login_required(login_url='login')
def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.usuario = request.user
            tarea.save()
            return redirect('Siete:lista_tareas')
    else:
        form = TareaForm()
    
    return render(request, 'Siete/crear_tarea.html', {'form': form})
