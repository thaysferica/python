peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)

print(f"\nSeu IMC é: {imc:.1f}")

if imc < 18.5:
    print("Status: Abaixo do Peso")
elif 18.5 <= imc < 25:
    print("Status: Peso ideal")
elif 25 <= imc < 30:
    print("Status: Sobrepeso")
elif 30 <= imc < 40:
    print("Status: Obesidade")
else:
    print("Status: Obesidade mórbida")