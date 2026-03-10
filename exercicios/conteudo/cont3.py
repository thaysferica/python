nome= input ('qual é seu nome?')
print ('prazer em conhece-lo {:20}!'.format(nome))
print ('prazer em conhece-lo {:>20}!'.format(nome)) #espaçamento para a direita
print ('prazer em conhece-lo {:<20}!'.format(nome)) #espaçamento para a esquerda
print ('prazer em conhece-lo {:^20}!'.format(nome)) #alinhamento no centro
nu1 = int (input('digite um valor'))
nu2 = int (input('digite outro valor'))
soma = (nu1+nu2) #ultiliza variável quando vai se ultilizar em outra parte do código
print ('a soma é {}'.format(soma))