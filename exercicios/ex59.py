sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()

# Verifica se a string está vazia ou se o primeiro caractere não é M ou F
while not sexo or sexo[0] not in 'MF':
    sexo = str(input('Dados inconsistentes, informe novamente: ')).strip().upper()

# Pega apenas a primeira letra para exibir
sexo = sexo[0]
print(f'O seu sexo é {sexo}')
