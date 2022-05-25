"""
Classes
Programação Orientada a Objetos está presente em todas as linguagens de
programação mais modernas segue o paradigma de programação
onde você tenta retratar coisas do mundo
real como objetos dentro do seu programa
"""
from pessoa import Pessoa
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
