from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import NewUserForm

def inicio(request):
    return render(request, 'inicio.html')

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("bienvenida") 
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

    form = NewUserForm()
    return render(request=request, template_name="main/register.html", context={"register_form":form})

def login_request(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("bienvenida")
        else:
            return render(request, "main/login.html", {"error": "Invalid username or password"})
    else:
        return render(request, "main/login.html")

def bienvenida(request):
    if request.user.is_authenticated:
        return render(request, "main/bienvenida.html")
    else:
        return redirect("login")
