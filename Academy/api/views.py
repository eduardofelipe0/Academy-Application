from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import *
from django.contrib import messages

# Create your views here.
@login_required
def home(request):
    images = ['foto1.jpg', 'foto2.jpg', 'foto3.jpg']
    return render(request, "home.html", {'images': images})

def signup(request, template_name='registration/login.html'):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Cadastro realizado com sucesso! Você está logado agora.')
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, template_name, {'form': form})

"""if request.method == 'POST':
        print(request.POST)
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, template_name, {'form': form})"""
