contagem = (
    'zero', 'um', 'dois', 'três', 'quatro',
    'cinco', 'seis', 'sete', 'oito', 'nove',
    'dez', 'onze', 'doze', 'treze', 'catorze',
    'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
)

digitado = int(input("digite um numero entre 0 e 20: "))
while True:
    if digitado < 0 or digitado >20:
        digitado = int(input("tente novamente. digite um numero entre 0 e 20: "))
    else:
        break
print(f"vove digitou o numero {contagem[digitado]} ")