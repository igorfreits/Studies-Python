from produto.models import Variacao
from django.contrib import messages
from django.shortcuts import redirect, render, reverse
from django.views.generic import ListView, DetailView
from django.views import View
from django.http import HttpResponse
from utils import utils
from . models import Pedido, ItemPedido
# Create your views here.


class DispatchLoginRequiredMixin(View):
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('perfil:criar')

        return super().dispatch(*args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(usuario=self.request.user)
        return qs


class Pagar(DispatchLoginRequiredMixin, DetailView):
    template_name = 'pedido/pagar.html'
    model = Pedido
    pk_url_kwarg = 'pk'
    context_object_name = 'pedido'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(usuario=self.request.user)
        return qs


class SalvarPedido(View):
    template_name = 'pedido/pagar.html'

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            messages.error(
                self.request, 'Você precisa estar logado para Continuar')
            return redirect('perfil:criar')
        cart = self.request.session.get('cart')
        carrinho_variacao_ids = [v for v in cart]
        bd_variacoes = list(Variacao.objects.select_related('produto').filter(
            id__in=carrinho_variacao_ids))

        for variacao in bd_variacoes:
            vid = str(variacao.id)
            estoque = variacao.estoque
            qtd_carrinho = cart[vid]['quantidade']
            preco_unt = cart[vid]['preco_unitario']
            preco_unt_promo = cart[vid]['preco_unitario_promocional']

            error_msg_estoque = ''

            if estoque < qtd_carrinho:
                cart[vid]['quantidade'] = estoque
                cart[vid]['preco_quantitativo'] = estoque * preco_unt
                cart[vid]['preco_quantitativo_promocional'] = estoque * \
                    preco_unt_promo

                error_msg_estoque = (
                    'Estoque insuficiente para alguns produtos do seu carrinho. '
                    'Reduzimos a quantidade desses produtos.'
                    'Por favor, verifique o seu carrinho.')
                if error_msg_estoque:
                    messages.error(self.request, error_msg_estoque)
                    self.request.session.save()
                    return redirect('produto:cart')

        qtd_total_carrinho = utils.cart_total_qtd(cart)
        valor_total_carrinho = utils.cart_totals(cart)

        pedido = Pedido(
            usuario=self.request.user,
            qtd_total=qtd_total_carrinho,
            total=valor_total_carrinho,
            status='C',

        )
        pedido.save()
        ItemPedido.objects.bulk_create(
            [
                ItemPedido(
                    pedido=pedido,
                    produto=v['produto_nome'],
                    produto_id=v['produto_id'],
                    variacao=v['variacao_nome'],
                    preco=v['preco_quantitativo'],
                    variacao_id=v['variacao_id'],
                    preco_promocional=v['preco_quantitativo_promocional'],
                    quantidade=v['quantidade'],
                    imagem=v['imagem'],

                )for v in cart.values()
            ]
        )
        del self.request.session['cart']
        return redirect(
            reverse('pedido:pagar', kwargs={'pk': pedido.id}))


class Detalhe(DispatchLoginRequiredMixin, DetailView):
    template_name = 'pedido/detalhe.html'
    model = Pedido
    context_object_name = 'pedido'
    pk_url_kwarg = 'pk'


class Lista(DispatchLoginRequiredMixin, ListView):
    template_name = 'pedido/lista.html'
    model = Pedido
    context_object_name = 'pedidos'
    paginate_by = 10
    ordering = ['-id']
