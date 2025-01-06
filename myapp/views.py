from django.shortcuts import render, redirect
from .models import Cadastro
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def cadastrar(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']

        if Cadastro.objects.filter(email=email).exists():
            messages.error(request, "Email já cadastrado!")
        else:
            Cadastro.objects.create(nome=nome, email=email)
            messages.success(request, "Cadastro realizado com sucesso!")

    return redirect('home')