from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tarea



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
        fields = ['nombre', 'descripcion', 'fecha_vencimiento']


