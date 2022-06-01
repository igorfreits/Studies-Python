"""
Classes
Programação Orientada a Objetos está presente em todas as linguagens de
programação mais modernas segue o paradigma de programação
onde você tenta retratar coisas do mundo
real como objetos dentro do seu programa
"""
# Modulo classe Pessoa
# Precisa de um molde usando o class
# Usar letra maiúscula no inicio
# Método é uma função que pertence a classe
# __init__ inicializa o objeto quando vai criar uma instância daquela classe

# Pode usar a nome da class com maiúsculo
# Método é uma função que pertence a classe
# self - instancia EX: (pessoa1)


# criar um objeto a partir do meu molde que é a minha classe
# eu tenho que instância para esse objeto
# e posso ter varias "Pessoas" vindo do mesmo molde
# Se não houver os () não sera executado
"""PascalCase - significa que todas as palavras iniciam com letra maiúscula e nada é usado para separá-las,
como em: MinhaClasse, Classe, MeuObjeto, MeuProgramaMuitoLegal.
Essa á a convenção utilizada para classes em Python;

camelCase - a única diferença de camelCase para PascalCase é a primeira letra. Em camelCase a primeira letra
sempre será minúscula e o restante das palavras deverá iniciar com letra maiúscula.
Como em: minhaFunção, funçãoDeSoma, etc... Essa conversão não é usada em Python
(apesar de eu confundir as duas e às vezes acabar chamando camelCase de PascalCase ou vice-versa, mas agora você sabe a diferença);

snake_case - este é o padrão usado em Python para definir qualquer coisa que não for uma classe.
Todas as letras serão minúsculas e separadas por um underline, como em: minha_variável, função_legal, soma.

Os padrões usados em Python são: snake_case para qualquer coisa e PascalCase para classes.
"""




from datetime import datetime
class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))
    """Se for criado uma variável dentro do __init__
    ela so estará disponível dentro do escopo do __init__"""

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return

        if self.falando:
            print(f'{self.nome} já está falando.')
            return

        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return

        print(f'{self.nome} parou de falar.')
        self.falando = False

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return

        if self.falando:
            print(f'{self.nome} não pode comer falando.')
            return

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return

        print(f'{self.nome} parou de comer.')
        self.comendo = False

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade


pessoa1 = Pessoa('a', 1)
pessoa2 = Pessoa('b', 2)
# São pessoas, mas estão em locais diferentes da memoria
# Estamos criando um objeto a partir de um classe
# Estamos  utilizando o molde para criar uma "Pessoa"
print(pessoa1)  # <pessoa.Pessoa object at 0x000002205979BFD0>
print(pessoa2)  # <pessoa.Pessoa object at 0x000002205979BF10>

# A variável nome esta presente somente na "pessoa1"
# Variáveis de classe são chamados de atributos(Funções)
pessoa1.nome = 'Igor'
pessoa2.nome = 'Michele'

pessoa1 = Pessoa('Igor', 23)  # parâmetros nome e idade da classe
pessoa2 = Pessoa('Michele', 21)

pessoa1.comer('bolacha')
pessoa1.comer('bolacha')
pessoa1.parar_comer()
pessoa1.parar_comer()
pessoa1.comer('bolacha')

pessoa1.falar('Computador')
pessoa1.parar_comer()
pessoa1.falar('Jogos')
pessoa1.falar('Jogos')
pessoa1.comer('Danone')

pessoa2.falar('chocolate')
pessoa1.parar_comer()
pessoa2.parar_falar()
pessoa2.comer('chocolate')

print(pessoa1.get_ano_nascimento())
print(pessoa2.get_ano_nascimento())
