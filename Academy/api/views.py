from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.

@login_required
def home(request):
    images = ['foto1.jpg', 'foto2.jpg', 'foto3.jpg']
    return render(request, "home.html", {'images': images})

@login_required
def listar_usuarios(request, template_name='listar_usuarios.html'):
    user = User.objects.all()
    users = {'lista': user}
    return render(request, template_name, users)

@login_required
def cadastrar_usuario(request, template_name='criar_usuario.html'):
    if request.method == "GET":
        return render(request, template_name)
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Já existe um usuário cadastrado com esse username')

        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        user.save()

        return HttpResponse('Usuário cadastrado com sucesso!')
