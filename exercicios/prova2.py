import random
aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
lista_alunos = [aluno1, aluno2, aluno3]
escolhido = random.choice(lista_alunos)
print(f"O aluno sorteado para apagar o quadro é: {escolhido}")
