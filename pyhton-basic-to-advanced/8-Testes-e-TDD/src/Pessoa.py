"""aula-113-Unittest#3"""
import requests


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        self.dados_obtidos = False

    def obter_todos_os_dados(self):
        resposta = requests.get('Fake URL')

        if resposta.ok:
            self.dados_obtidos = True
            return 'CONECTADO'

        else:
            self.dados_obtidos = False
            return 'Erro 404'
