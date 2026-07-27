print('-' * 15)
print('loja super baratão')
print('-' * 15)
total = totmil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    total += preco
    
    if preco > 1000:
        totmil += 1
        
    if cont == 1:
        menor = preco
        barato = produto
