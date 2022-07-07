from django.conf import settings
import os
from PIL import Image
from django.db import models


# Create your models here.


class Produto(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    descricao_curta = models.TextField(
        max_length=200, verbose_name='Descrição Curta')
    descricao_longa = models.TextField(verbose_name='Descrição Longa')
    imagem = models.ImageField(
        upload_to='produto_imagens/%Y/%m', verbose_name='Imagem')
    slug = models.SlugField(unique=True, verbose_name='Slug')
    preco_marketing = models.FloatField(verbose_name='Preço Marketing')
    preco_marketing_promocional = models.FloatField(
        default=0, verbose_name='Preço Marketing Promocional')
    tipo = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V', 'Variável',),
            ('S', 'Simples',)), verbose_name='Tipo')

    @staticmethod
    def resize_image(img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size

        if original_width <= new_width:
            img_pil.close()
            return
        new_height = round((original_height * new_width) / original_width)
        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
        new_img.save(img_full_path,
                     optimize=True,
                     quality=50

                     )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        max_image_size = (800)

        if self.imagem:
            self.resize_image(self.imagem, max_image_size)

    def __str__(self):
        return self.nome


class Variacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, blank=True, null=True)
    preco = models.FloatField()
    preco_promocional = models.FloatField(default=0)
    estoque = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.nome or self.produto.nome

    class Meta:
        verbose_name = 'Variação'
        verbose_name_plural = 'Variações'
