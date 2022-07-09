from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse

# Create your views here.


class Criar(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Criar")


class Update(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Update")


class Login(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Login")


class Logout(ListView):
    def get(self, *args, **kwargs):
        return HttpResponse("Logout")
