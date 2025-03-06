"""
Métodos de classes
"""
# métodos de classe são métodos que são relativos à classe inteira
# Método de instancia - Precisam precisam de umas instancia (self)
# Classmethod - Precisa da classe em si
# Classe - Objeto do mundo real
# Atributos - Características
# Métodos - Funções(Ação)
# Deve ter inicial maiúsculo e nao pode conter espaços

"""class ControleRemoto:  # Objeto
    características
    -cor
    -altura
    -profundidade
    -largura

métodos do ControleRemoto:
    -passar de canal
    -mexer no volume
    -abrir  Netflix
    -desligar a tv"""


class ControleRemoto:
    # Definir Função __init__ (Inicializa a classe com os atributos)
    # Exemplo:
    # "Netflix" precisa criar uma conta que precisa do:
    # email,nome, cartão de crédito

    def __init__(self, cor, altura, profundidade, largura):
        # parameter que devem ser passados
        # self - Referencia a uma característica do controle remoto

        self.cor = cor  # característica cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura
        # marca = marca - Não esta atribuído a "marca" no ControleRemoto

    def passar_canal(self, botão):
        if botão == '+':
            print('Aumentar o canal')
        elif botão == '-':
            print('Diminuir o canal')


controle_remoto1 = ControleRemoto('Preto', '10cm', '20cm', '2cm')
controle_remoto2 = ControleRemoto('Cinza', '10cm', '20cm', '2cm')
print(controle_remoto1.cor)

controle_remoto1.passar_canal('+')

# Netflix


class Netflix:
    def __init__(self, nome, email, plano):  # Características
        self.nome = nome
        self.email = email
        # Variável sozinha so é acessada dentro da função init
        self.list_plans = ['basic', 'premium']
        if plano in self.list_plans:
            self.plano = plano
        else:
            raise Exception('Plano invalido')

        self.plano = plano

    def mudar_plan(self, new_plano):
        if new_plano in self.list_plans:
            self.plano = new_plano
            return self.plano
        else:
            print('Plano invalido')

    def ver_film(self, film, plan_film):
        if self.plano == plan_film:
            print(f'Ver filme {film}')
        elif self.plano == 'premium':
            print(f'Ver filme {film}')
        elif self.plano == 'basic' and plan_film == 'premium':
            print('Faça upgrade para o plano premiu para ver o filme')
        else:
            print('Plano invalido')


client = Netflix('Igor', 'Colomkiuns@gmail.com', 'basic')


print(client.plano)
client.ver_film('Harry potter', 'premium')

# Button upgrade
print(client.mudar_plan('premium'))
print(client.plano)
client.ver_film('Harry potter', 'premium')

# Udemy


class Pessoa:
    ano_atual = 2022
    # Atributo de classe e esta disponível para todas as instancias

    def __init__(self, nome, idade):
        # Estão relacionados a instancia(self) e precisam receber uma instancia
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        # A variável so esta disponível dentro daa função
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)


p1 = Pessoa('Igor', 23)
p1.get_ano_nascimento()

p1 = Pessoa.por_ano_nascimento('Igor', 1999)

print(p1.nome, p1.idade)
p1.get_ano_nascimento()
