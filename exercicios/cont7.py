frase = ('curso de análise e desenvolvimento de sistemas')
print(frase[3]) #isso mostra o espaço da memória
print(frase[3:46]) #intervalo de caracteres menos o último
print(frase[3:45:2]) #pula de dois em dois
print(frase[:7]) #pega do inicio ate o caracter que vc escolheu
print(frase[7:]) #pega do caracter que  vc escolheu ate o final
print(frase[41::5]) #pega do caracter que vc escolheu pulando de 3 em 3
print (len(frase)) #esse metodo conta a quantidade de caracter
print(frase.count('t')) #procura um caracter especifico na variável
print(frase.count('t', 0,7)) #procura um caracter especifico dentro de um ccomentario especifico
print(frase.find('análise')) #find mostra a partir de qual indice começa a pesquisa
print(frase.find('android')) #o resultado -1 indica que não tem essa sequencia na variável
print ('curso'in frase) #o in verifica se aquele conjunto de string esta na variável
print (frase.replace('curso', 'instituição')) #troca a palavra
print (frase.upper()) #deixa em maiusculo
print (frase.lower()) #deixa em minuscculo
print (frase.capitalize()) #deixa a primeira letra da primeira palavra em maiusculo
print (frase.title()) #deixa todas as primeiras letras em maiusculo
print (frase.strip()) #tira o espaço em branco do inicio e do final
print (frase.rstrip()) #tira o espaço em branco da direita
print (frase.lstrip()) #tira o espaço em branco da esquerda
print (frase.split()) #vai transformar o valor da variavel em uma lista
print ('%'.join(frase)) #uni o simbolo em cada parte do split