from datetime import date

# Entrada do ano de nascimento
ano = int(input("Ano de nascimento: "))

# Cálculo da idade
idade = date.today().year - ano

# Cálculo do tempo passado ou faltante para o alistamento
tempopassado = idade - 18
tempofaltante = 18 - idade

# Exibição da idade
print("Quem nasceu em {} tem {} anos.".format(ano, idade))

# Verificação das condições de alistamento
if idade > 18:
    print("Você já deveria ter se alistado há {} anos.".format(tempopassado))
elif idade < 18:
    print("Você ainda não tem idade para se alistar. Faltam {} anos.".format(tempofaltante))
else:
    print("Você deve se alistar este ano.")