#cont =1 
#while True:
  #  print (cont, "->", end="")
 #   cont +=1
#print ("acabou") 

n = s = 0
while True:
    n = int(input('digite um numero'))
    if n == 999:
      break
    s+=n
print (f'a soma vale {s}')        