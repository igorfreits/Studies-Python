from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Pedido(models.Model):
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Usuário')
    total = models.FloatField(verbose_name='Total')
    status = models.CharField(
        default="C",
        max_length=1, verbose_name='Status',
        choices=(
            ('A', 'Aprovado'),
            ('C', 'Criado'),
            ('R', 'Reprovado'),
            ('P', 'Pendente'),
            ('E', 'Enviado'),
            ('F', 'Finalizado'),
        )
    )

    def __str__(self):
        return self.usuario.username


class ItemPedido(models.Model):
    pedido = models.ForeignKey(
        Pedido, on_delete=models.CASCADE, verbose_name='Pedido')
    produto = models.CharField(max_length=255, verbose_name='Produto')
    produto_id = models.IntegerField(verbose_name='Produto ID')
    variacao = models.CharField(max_length=255, verbose_name='Variação')
    variacao_id = models.PositiveIntegerField(verbose_name='Variação ID')
    preco = models.FloatField(verbose_name='Preço')
    preco_promocional = models.FloatField(
        default=0, verbose_name='Preço Promocional')
    quantidade = models.PositiveIntegerField(verbose_name='Quantidade')
    imagem = models.CharField(max_length=2000, verbose_name='Imagem')

    def __str__(self):
        return f'Item do {self.pedido}'

    class Meta:
        verbose_name = 'Item do Pedido'
        verbose_name_plural = 'Itens do Pedido'
