from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'Siete'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('login/', views.login_request, name='login'),
    path('logout/', LogoutView.as_view(next_page='Siete:inicio'), name='logout'),
    path('bienvenido/', views.bienvenido, name='bienvenido'),
    path("register", views.register_request, name="register"),
    path('tareas/', views.lista_tareas, name='lista_tareas'),
    path('tareas/crear/', views.crear_tarea, name='crear_tarea'),
    path('crear_tarea/', views.crear_tarea, name='crear_tarea'),
    path('tareas/editar/<int:id>', views.editar_tarea, name='editar_tarea'),
    path('tarea/<int:id_tarea>/', views.ver_tarea, name='ver_tarea'),
    path('tarea/<int:id_tarea>/editar/', views.editar_tarea, name='editar_tarea'),
    path('tarea/<int:id_tarea>/eliminar/', views.eliminar_tarea, name='eliminar_tarea'),
    path('tarea/<int:id_tarea>/completar/', views.completar_tarea, name='completar_tarea'),
]

