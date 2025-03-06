from django.db import models
from posts.models import Post
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Comentarios(models.Model):
    nome_comentario = models.CharField(max_length=150, verbose_name='Nome')
    email_comentario = models.EmailField(verbose_name='E-mail')
    comentario = models.TextField(verbose_name='Comentário')
    post_comentario = models.ForeignKey(
        Post, on_delete=models.CASCADE, verbose_name='Post comentado')
    usuario_comentario = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, blank=True, null=True)
    data_comentario = models.DateField(
        default=timezone.now, verbose_name='Data')
    publicacao_comentario = models.BooleanField(
        default=False, verbose_name='Publicado')

    def __str__(self):
        return self.nome_comentario

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'
