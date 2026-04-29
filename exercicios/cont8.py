#tempo = int(input('quantos anos tem o seu carro?'))
#if tempo<=3:
   # print ('carro novo')
#else:
   # print ('carro velho')
   # print ('--fim--')

#tempo = int(input('quantos anos tem o seu carro?'))
#print ('carro novo' if tempo <=3 else 'carro velho')

#nome = str(input('qual é o seu nome?'))
#if nome == 'thaynara':
 #   print ('que nome lindo vc tem')
#else: 
 #   print ('o seu nome é tão normal')
#print ('bom dia{}'.format(nome))

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = (n1 + n2) / 2
print("A sua média foi {:.1f}".format(m))

if m >= 6.0:
    print("A sua média foi boa! Parabéns")
else:
    print("Sua média foi ruim! Estude mais")

print("Parabéns" if m >= 6 else "Estude mais")