from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import Tarea, Etiqueta
from .forms import FiltroTareasForm, TareaForm, NewUserForm
from django.shortcuts import get_object_or_404
from .forms import ObservacionForm
from django.utils import timezone
from django.http import HttpResponseForbidden   # Import HttpResponseForbidden
from django.contrib.auth.models import User


# Resto de tu código...


def inicio(request):
    return render(request, 'inicio.html')

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("Siete:bienvenido") 
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
    

@login_required(login_url='login')
def lista_tareas(request):
    # Inicialmente, obtén todas las tareas del usuario
    tareas = Tarea.objects.filter(usuario=request.user, completada=False).order_by('fecha_vencimiento')

    # Crea un formulario FiltroTareasForm con las etiquetas del usuario actual
    form = FiltroTareasForm(request.GET or None)
    form.fields['etiqueta'].queryset = Etiqueta.objects.filter(usuario=request.user)

    # Si el formulario es válido, aplica el filtro
    if form.is_valid():
        if form.cleaned_data['titulo']:
            tareas = tareas.filter(nombre__icontains=form.cleaned_data['titulo'])
        if form.cleaned_data['etiqueta']:
            tareas = tareas.filter(etiquetas=form.cleaned_data['etiqueta'])

    return render(request, 'Siete/lista_tareas.html', {'form': form, 'tareas': tareas})



# views.py
@login_required(login_url='login')
def ver_tarea(request, id_tarea):
    tarea = get_object_or_404(Tarea, id=id_tarea)
    
    if tarea.usuario != request.user:
        return HttpResponseForbidden()

    if request.method == 'POST':
        form = ObservacionForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('Siete:lista_tareas')  # Redirecciona a la vista de lista de tareas
    else:
        form = ObservacionForm(instance=tarea)

    return render(request, 'Siete/ver_tarea.html', {'form': form, 'tarea': tarea})


def editar_tarea(request, id_tarea):
    tarea = Tarea.objects.get(id=id_tarea)

    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            tarea = form.save()
            return redirect('Siete:ver_tarea', id_tarea=tarea.id)
    else:
        form = TareaForm(instance=tarea)

    return render(request, 'Siete/editar_tarea.html', {'form': form})

@login_required(login_url='login')
def eliminar_tarea(request, id_tarea):
    tarea = get_object_or_404(Tarea, id=id_tarea)

    if tarea.usuario != request.user:
        return HttpResponseForbidden()

    tarea.delete()
    return redirect('Siete:lista_tareas')

@login_required(login_url='login')
def completar_tarea(request, id_tarea):
    tarea = get_object_or_404(Tarea, id=id_tarea)

    if tarea.usuario != request.user:
        return HttpResponseForbidden()

    tarea.completada = True
    tarea.save()
    return redirect('Siete:lista_tareas')

# views.py
@login_required(login_url='login')
def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.usuario = request.user
            tarea.save()
            form.save_m2m()  # Para guardar las relaciones ManyToMany
            return redirect('Siete:lista_tareas')
    else:
        form = TareaForm()
        form.fields['usuario_asignado'].queryset = User.objects.exclude(id=request.user.id)
    return render(request, 'Siete/crear_tarea.html', {'form': form})

