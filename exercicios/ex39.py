# Entrada do número inteiro
n1 = int(input("Digite um número: "))

# Menu de opções para o usuário escolher a base de conversão
print('''Escolha uma das bases para a conversão:
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')  # As 3 aspas permitem escrever em mais de uma linha

# Entrada da opção do usuário
opcao = int(input("Sua opção: "))

# Verificação da opção escolhida e conversão
if opcao == 1:
    print("{} convertido para BINÁRIO é igual a {}".format(n1, bin(n1)[2:]))
elif opcao == 2:
    print("{} convertido para OCTAL é igual a {}".format(n1, oct(n1)[2:]))
elif opcao == 3:
    print("{} convertido para HEXADECIMAL é igual a {}".format(n1, hex(n1)[2:]))
else:
    print("Opção inválida! Tente novamente.")