salario = float(input('qual é o salario do funcionario?'))
aumento15 = salario + (salario*0.15)
aumento10 = salario + (salario*0.10)
if salario > 1250:
    print("Quem ganhava R${} passa a ganhar R${}".
    format(salario, aumento10))
else:
    print("Quem ganhava R${} passa a ganhar R${}".
format(salario, aumento15))