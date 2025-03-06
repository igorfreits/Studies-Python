from django.forms import ModelForm
from .models import Comentarios
import requests


class FormComentario(ModelForm):
    def clean(self):
        raw_data = self.data
        recaptcha_response = raw_data.get('g-recaptcha-response')

        recaptcha_request = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data={
                'secret': '6LchENEgAAAAAPPnZFKry2Wvy3pkLdz9D4PL5XKC',
                'response': recaptcha_response
            }
        )
        recaptcha_result = recaptcha_request.json()
        if not recaptcha_result.get('success'):
            self.add_error(
                'comentario',
                'Desculpe Mr. Robot, ocorreu um erro'
            )

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
