n1 = float(input("Digite o primeiro numero "))
n2 = float(input("Digite o segundo numero "))
n3 = float(input("Digite o terceiro numero "))

maior = n1
menor = n1
if n2 > n1 and n2>n3:
    maior = n2
if n3 > n1 and n3>n2:
    maior = n3
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print("o maior numero digitado foi {}".format(maior))
print("o menor numero é {}" .format(menor))
