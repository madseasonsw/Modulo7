from django.contrib import admin
from .models import Etiqueta  # Asegúrate de que Etiqueta está importado desde models

admin.site.register(Etiqueta)  # Esto registra el modelo Etiqueta en el administrador
