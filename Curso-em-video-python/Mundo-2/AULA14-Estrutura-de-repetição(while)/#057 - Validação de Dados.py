sexo = str(input('Informe o seu sexo [M/F} ')).upper().strip()[0]

while sexo not in 'M /  F':
    sexo = str(input('Dados inválidos. Por favor, informe o seu sexo: '))
print(f'Sexo {sexo} Cadastrado com sucesso!')
