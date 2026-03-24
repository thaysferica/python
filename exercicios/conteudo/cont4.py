#import math 
#num = int (input('digite um numero')) 
#raiz = math.sqrt(num) 
#print('a raiz de {} é igual a {}'.format(num,math.ceil(raiz))) 
#print('a raiz de {} é igual a {}'.format(num,math.floor(raiz)))

#importando funcionalidades especificas
from math import sqrt, ceil, floor
num = int(input('digite um numero'))
raiz = sqrt(num)  
print('a raiz de {} é igual a {}'.format(num,ceil(raiz))) 