from django.forms import ModelForm
from .models import Comentarios


class FormComentario(ModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data
        nome = cleaned_data.get('nome_comentario')
        email = cleaned_data.get('email_comentario')
        comentario = cleaned_data.get('comentario')

        if len(nome) < 5:
            self.add_error(
                'nome_comentario',
                'Nome precisa ter mais que 5 caracteres.'
            )

    class Meta:
        model = Comentarios
        fields = ('nome_comentario', 'email_comentario', 'comentario')
