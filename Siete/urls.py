from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('login/', views.login_request, name='login'),
    path('logout/', LogoutView.as_view(next_page='inicio'), name='logout'),
    path('bienvenida/', views.bienvenida, name='bienvenida'),
    path("register", views.register_request, name="register"),
]

