from django import forms
from .models import *


# Create your forms here.
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['name', 'username', 'password', 'role', 'academy_id']
        widgets = {
            'password': forms.PasswordInput()
        }
