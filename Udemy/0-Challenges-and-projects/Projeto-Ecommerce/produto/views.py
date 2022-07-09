from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from . import models
# Create your views here.


class ListaProdutos(ListView):
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'


class DetalheProduto(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Detalhe Produto")


class AddToCart(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Add to Cart")


class RemoveFromCart(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Remove from Cart")


class Cart(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Cart")


class Finalizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Finalizar")
