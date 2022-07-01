from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from . models import FormContato
# Create your views here.


def login(request):

    if request.method != 'POST':
        return render(request, 'accounts/login.html')
    usuário = request.POST.get('usuário')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuário, password=senha)
    if not user:
        messages.error(request, 'Usuário ou senha inválidos')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Você foi logado com sucesso')
        return redirect('dashboard')


def logout(request):
    auth.logout(request)
    messages.success(request, 'Você foi deslogado com sucesso')
    return redirect('index')


def register(request):
    if request.method != 'POST':
        return render(request, 'accounts/register.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuário = request.POST.get('usuário')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not nome or not sobrenome or not email or not usuário or not senha \
            or not senha2:
        messages.error(request, 'Nenhum campo pode estar vazio.')
        return render(request, 'accounts/register.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'Email inválido')
        return render(request, 'accounts/register.html')

    if len(senha) < 6:
        messages.error(request, 'A senha precisa ter 6 caracteres ou mais')
        return render(request, 'accounts/register.html')

    if len(usuário) < 6:
        messages.error(request, 'O usuário precisa ter 6 caracteres ou mais')
        return render(request, 'accounts/register.html')

    if senha != senha2:
        messages.error(request, 'Senhas não conferem.')
        return render(request, 'accounts/register.html')

    if User.objects.filter(username=usuário).exists():
        messages.error(request, 'E-mail ja existente')
        return render(request, 'accounts/register.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'Usuário ja existente')
        return render(request, 'accounts/register.html')

    messages.success(request, 'Cadastrado com sucesso!\n'
                     'Realize o login')
    user = User.objects.create(username=usuário, email=email,
                               password=senha, first_name=nome,
                               last_name=sobrenome)
    user.save()
    return redirect('login')


@login_required(redirect_field_name='login')
def dashboard(request):
    if request.method != 'POST':
        form = FormContato()
        return render(request, 'accounts/dashboard.html', {'form': form})
    form = FormContato(request.POST, request.FILES)

    if not form.is_valid():
        messages.error(request, 'Erro ao enviar o formulário')
        form = FormContato(request.POST)
        return render(request, 'accounts/dashboard.html', {'form': form})

    descrição = request.POST.get('descrição')
    if len(descrição) < 5:
        messages.error(request, 'Descrição precisar ter mais que 5 caracteres')
        form = FormContato(request.POST)
        return render(request, 'accounts/dashboard.html', {'form': form})

    form.save()
    messages.success(
        request, f'O contato {request.POST.get("nome")}  '
        'foi cadastrado com sucesso!')
    return redirect('dashboard')
