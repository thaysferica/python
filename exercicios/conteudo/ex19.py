import math
co = float (input('comprimento do cateto oposto:'))
ca = float (input('comprimento do cateto adjacente:'))
a = math.hypot (co, ca)
print ('a hipotenusa vai medir {}'.format(a))