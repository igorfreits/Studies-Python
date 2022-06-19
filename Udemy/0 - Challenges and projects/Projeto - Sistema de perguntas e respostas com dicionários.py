perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 + 2? ',
        'respostas': {'a': '1', 'b': '5', 'c': '4', },
        'resposta_certa': 'c',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3 * 2 ',
        'respostas': {'a': '6', 'b': '10', 'c': '9', },
        'resposta_certa': 'a',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é a raiz quadrada de 100? ',
        'respostas': {'a': '100', 'b': '10', 'c': '1000', },
        'resposta_certa': 'b',
    },
    'Pergunta 4': {
        'pergunta': 'Qual a resposta para a Grande Pergunta sobre a Vida, o Universo e Tudo o Mais ',
        'respostas': {'a': '69', 'b': '∞', 'c': '42', },
        'resposta_certa': 'c',
    },
    'Pergunta 5': {
        'pergunta': 'Quanto é vale π (pi) ',
        'respostas': {'a': '3.14', 'b': '44', 'c': '1000', },
        'resposta_certa': 'a',
    },
}

print()
respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('RESPOSTAS: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('SUA RESPOSTA: ')

    if resposta_usuario == pv['resposta_certa']:
        print('VOCÊ ACERTOU')
        respostas_certas +=1
    else:
        print('VOCÊ ERROU')

    print()
qtd_perguntas = len(perguntas)
porcetagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Você acertou {respostas_certas} respostas')
print(f'Sua porcentagem de acerto foi de {porcetagem_acerto:.2f}%')