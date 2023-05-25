from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tarea
from .models import Etiqueta



class FiltroTareasForm(forms.Form):
    nombre = forms.CharField(required=False)
    etiqueta = forms.ModelChoiceField(queryset=Etiqueta.objects.none(), required=False)



class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    

class TareaForm(forms.ModelForm):
    fecha_vencimiento = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Tarea
        fields = ['nombre', 'descripcion', 'fecha_vencimiento', 'etiquetas', 'observaciones']
        widgets = {
            'etiquetas': forms.CheckboxSelectMultiple
        }


