from django.contrib import admin
from .models import Comentarios


class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_comentario', 'email_comentario',
                    'post_comentario', 'data_comentario',
                    'publicacao_comentario')
    list_editable = ('publicacao_comentario',)
    list_display_links = ('id', 'nome_comentario', 'email_comentario',)


admin.site.register(Comentarios, ComentarioAdmin)
