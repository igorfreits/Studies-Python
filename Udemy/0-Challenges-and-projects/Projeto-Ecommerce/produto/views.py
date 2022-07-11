from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
from matplotlib.pyplot import get
from . import models

# Create your views here.


class ListaProdutos(ListView):
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = 3


class DetalheProduto(DetailView):
    model = models.Produto
    template_name = 'produto/detalhe.html'
    context_object_name = 'produto'
    slug_url_kwarg = 'slug'


class AddToCart(View):
    def get(self, request, *args, **kwargs):
        http_referer = self.request.META.get(
            'HTTP_REFERER',
            reverse('produto:lista')
        )
        variacao_id = self.request.GET.get('vid')

        if not variacao_id:
            messages.error(
                request,
                'O produto não existe'
            )

        variacao = get_object_or_404(models.Variacao, id=variacao_id)

        if not self.request.session.get('carrinho'):
            self.request.session['carrinho'] = {}
            self.request.session.save()

        carrinho = self.request.session['carrinho']

        if variacao_id in carrinho:
            pass
        else:
            pass

        messages.success(
            self.request, f'O item {variacao.nome} foi adicionado ao carrinho')
        return redirect(http_referer)
        # return HttpResponse(f'{variacao.nome} adicionado ao carrinho')


class RemoveFromCart(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Remove from Cart")


class Cart(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Cart")


class Finalizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Finalizar")
