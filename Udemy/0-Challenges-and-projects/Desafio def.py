"""
1 - Crie uma função que exibe uma saudação com os parâmetros saudação e nome.
"""


from random import randint


def saudacao(msg='Olá', nome='Usuário'):
    print(msg, nome)


saudacao('Olá', 'Igor')
saudacao(nome='Michele', msg='Hello')

"""
2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre 
eles.
"""


def soma(n1, n2, n3):
    print(int(n1 + n2 + n3))


soma(1, 4, 5)
soma(39, 12, 5)
soma(12, 77, 14)

"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um
percentual (ex. 10%). Retorne (return) o valor do primeiro número somado
do aumento do percentual do mesmo.
"""


def promocao(valor, desconto):
    return valor * desconto / 100


print(promocao(2000, 10))


"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da
função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o
número enviado.
"""


def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return f'FIZZBUZZ, {n} é divisível por 3 e por 5'
    if n % 3 == 0:
        return f'FIZZ, {n} é divisível por 3'
    if n % 5 == 0:
        return f'BUZZ, {n} é divisível por 5'
    return n


print(fb(50))
print(fb(15))
print(fb(27))
print(fb(22))


for i in range(100):
    aleatorio = randint(0, 100)
    print(fb(aleatorio))
