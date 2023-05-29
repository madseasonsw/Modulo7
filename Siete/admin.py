from django.contrib import admin
from .models import Etiqueta  # Asegúrate de que Etiqueta está importado desde models
from .models import Prioridad
from .models import Tarea

admin.site.register(Etiqueta)  # Esto registra el modelo Etiqueta en el administrador
admin.site.register(Prioridad)
admin.site.register(Tarea)
