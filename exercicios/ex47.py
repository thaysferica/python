#from random import randint
#from time import sleep
#print('''Suas opções
#[0] pedra
#[1] papel
#[2] Tesoura''')
#jogada =int(input("Qual é a sua jogada? "))
#jogadapc= randint(0,2)
#Itens = ("Pedra", "Papel", "Tesoura")
#print("jo")
#sleep(1)
#print("ken")
#sleep(1)
#print("po !!!")
#sleep(1)
#print("-=-" * 10)
#print(f'''computador jogou {Itens [jogadapc]}
#jogador jogou {Itens [jogada]}''')
#print("-=-" * 10)
#if jogadapc== 0 and jogada== 2 or jogadapc== 1 and jogada ==0 or jogadapc ==2 and jogada== 1:
 #   print("Computador vence")
#if jogada== 0 and jogadapc== 2 or jogada== 1 and jogadapc ==0 or jogada ==2 and jogadapc== 1:
 #   print("jogador vence")

#else:
    #print("empate")

from random import randint
from time import sleep

print("-=" * 15)
print("  JOKENPÔ COM REGRAS INVERTIDAS ")
print("-=" * 15)

print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogada = int(input("Qual é a sua jogada? "))
jogadapc = randint(0, 2)
itens = ("Pedra", "Papel", "Tesoura")
if jogada < 0 or jogada > 2:
    print("Jogada inválida! Escolha entre 0, 1 ou 2.")
else:
    print("JO...")
    sleep(0.5)
    print("KEN...")
    sleep(0.5)
    print("PÔ!!!")
    sleep(0.5)

    print("-=-" * 10)
    print(f"Computador jogou: {itens[jogadapc]}")
    print(f"Jogador jogou: {itens[jogada]}")
    print("-=-" * 10)
    if jogada == jogadapc:
        print("EMPATE!")
        
    elif (jogada == 0 and jogadapc == 1) or \
         (jogada == 1 and jogadapc == 2) or \
         (jogada == 2 and jogadapc == 0):
        print("JOGADOR VENCEU! (Regra Invertida)")
        
    else:
        print("COMPUTADOR VENCEU! (Regra Invertida)")

