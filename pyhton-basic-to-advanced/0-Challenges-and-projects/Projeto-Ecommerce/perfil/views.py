from tabnanny import verbose
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from . import models
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import copy
from django.contrib import messages

# Create your views here.


class BasePerfil(View):
    template_name = 'perfil/criar.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)
        self.cart = copy.deepcopy(self.request.session.get('cart', {}))
        self.perfil = None

        if self.request.user.is_authenticated:
            self.perfil = models.Perfil.objects.filter(
                usuario=self.request.user).first()

            self.contexto = {
                'userform': forms.UserForm(data=self.request.POST or None,
                                           usuario=self.request.user,
                                           instance=self.request.user

                                           ),
                'perfilform': forms.PerfilForm(data=self.request.POST or None,
                                               instance=self.perfil),
            }
        else:
            self.contexto = {
                'userform': forms.UserForm(data=self.request.POST or None

                                           ),
                'perfilform': forms.PerfilForm(data=self.request.POST or None),

            }
        self.userform = self.contexto['userform']
        self.perfilform = self.contexto['perfilform']

        if self.request.user.is_authenticated:
            self.template_name = 'perfil/update.html'

        self.renderizar = render(
            self.request, self.template_name, self.contexto)

    def get(self, *args, **kwargs):
        return self.renderizar


class Criar(BasePerfil):
    def post(self, *args, **kwargs):
        if not self.userform.is_valid() or not self.perfilform.is_valid():
            messages.error(
                self.request, 'Existem erros no seu cadastro, '
                'verifique se os seus dados estão corretos')
            return self.renderizar

        username = self.userform.cleaned_data.get('username')
        password = self.userform.cleaned_data.get('password')
        email = self.userform.cleaned_data.get('email')
        first_name = self.userform.cleaned_data.get('first_name')
        last_name = self.userform.cleaned_data.get('last_name')

        # Usuário logado
        if self.request.user.is_authenticated:
            messages.success(self.request, 'Dados atualizados com sucesso!')

            usuario = get_object_or_404(
                User, username=self.request.user.username)

            usuario.username = username
            if password:
                usuario.set_password(password)

            usuario.email = email
            usuario.first_name = first_name
            usuario.last_name = last_name
            usuario.save()

            if not self.perfil:
                self.perfilform.cleaned_data['usuario'] = usuario
                perfil = models.Perfil(**self.perfilform.cleaned_data)
                perfil.save()
            else:
                perfil = self.perfilform.save(commit=False)
                perfil.usuario = usuario
                perfil.save()

        # Usuário não logado(novo)
        else:
            messages.success(self.request, 'Usuário criado com sucesso!')
            usuario = self.userform.save(commit=False)
            usuario.set_password(password)
            usuario.save()

            perfil = self.perfilform.save(commit=False)
            perfil.usuario = usuario
            perfil.save()

        if password:
            autentica = authenticate(self.request,
                                     username=usuario, password=password)
            if autentica:
                login(self.request, user=usuario)

        self.request.session['cart'] = self.cart
        self.request.session.save()
        return redirect('produto:cart')


class Update(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Update")


class Login(View):
    def post(self, *args, **kwargs):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')

        if not username and password:
            messages.error(self.request, 'Usuário ou senha inválidos')
            return redirect('perfil:criar')
        usuario = authenticate(
            self.request, username=username, password=password)

        if not usuario:
            messages.error(self.request, 'Usuário ou senha inválidos')
            return redirect('perfil:criar')

        login(self.request, user=usuario)
        messages.success(self.request, 'Usuário logado com sucesso')
        return redirect('produto:cart')


class Logout(ListView):
    def get(self, *args, **kwargs):
        cart = copy.deepcopy(self.request.session.get('cart', {}))
        logout(self.request)
        self.request.session['cart'] = cart
        self.request.session.save()
        messages.success(self.request, 'Você saiu com sucesso!')
        return redirect('produto:lista')
