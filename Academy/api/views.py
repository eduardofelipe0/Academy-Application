from django import forms
from django.shortcuts import render, redirect
from .models import *


# Create your views here.
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['name', 'username', 'password', 'role', 'academy_id']
        widgets = {
            'password': forms.PasswordInput()
        }

def listar_usuarios(request, template_name='listar_usuarios.html'):
    usuario = Usuario.objects.all()
    usuarios = {'lista': usuario}
    return render(request, template_name, usuarios)

def cadastrar_usuario(request, template_name='criar_usuario.html'):
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_usuarios')
    return render(request, template_name, {'form': form})

def login(request, template_name='login.html'):
    return render(request, template_name)
