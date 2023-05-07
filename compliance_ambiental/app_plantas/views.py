from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# Create your views here.
def home(request):
    return render(request, 'basico/home.html')

def cadastro(request):
    if request.method == "GET":
        return render(request, 'users/cadastro.html')
    else:
        username= request.POST.get('username')
        first_name= request.POST.get('nome')
        last_name= request.POST.get('sobrenome')
        email= request.POST.get('email')
        password= request.POST.get('senha')

        try:
            existe_usuario = User.objects.get(username=username)
            if existe_usuario:
                return HttpResponse(f"O nome de usuário - {username} - já existe, tente outro.")
        except User.DoesNotExist:
            novo_usuário = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password)
            novo_usuário.save()

        return HttpResponse(f"Cadastrado como: {username}") 
    # depois necessário logar esse mesmo usuário novo.

def login_app(request):
    if request.method == "GET":
        return render(request, 'users/login_app.html')
    else:
        username= request.POST.get('username')
        password= request.POST.get('senha')

        user= authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'users/plataforma.html')
        else:
            return HttpResponse('Usuário ou senha inválidos')

@login_required(login_url='/auth/login/')
def plataforma(request):
        return render(request, 'users/plataforma.html')