"""
Try, Except - Tratando Exceções
"""
# Exceções são erros - Se tiver um erro numa linha o código nao ira rodar
# não é uma boa pratica na programação
# Se usar o try o código continuar executando

# Formato simples
try:
    print(a)  # Vai tentar executar, se gerar algum erro ira cair no except
except:
    print('Erro')

try:
    a = []
    print(a[1])
    b = {}
    print(b[1])

except NameError as erro:
    print('Erro do desenvolvedor, false com ele')
except (IndexError, KeyError) as erro:
    print('Erro de indice ou chave')

# Caso voce achar que pode ocorrer outro erro
# Exception captura qualquer erro
except Exception as erro:
    print('Ocorreu um erro inesperado')

try:
    a = {}
except IndexError as error:
    print('Error')
else:  # Sera executado caso o bloco try nao ter erro
    ('Seu código foi executado com sucesso!')
    print(a)

finally:  # Sempre sera executado
    print('Finalmente')

try:
    a = 1/0
except:
    pass
finally:
    a = None  # ou ' '
print(a)

try:
    a = 0
    try:
        a = 1/0
    except:
        print('Erro')
except:
    print(' ')

"""
Em algum momento, você pode fazer algo no try que precisa ser finalizada,
por exemplo, abrir um arquivo, abrir um conexão de rede, etc etc...
Essas coisas abertas precisam ser fechadas,
porém, se houver erros antes de atingir o código de fechamento,
o que você abriu nunca será fechado. Então, é uma boa prática de programação,
assumir que o que você está fazendo pode gerar erros e usar o bloco finally
para finalizar/fechar o que tinha aberto antes
"""

print('Bora continuar...')
