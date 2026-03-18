km = float (input('quantos km foram percorridos?'))
dia = int (input('quantas km foram percorridos?'))
precodias = dia * 60 
precokm = km * 0.15
total = precodias + precokm
print ('o total a pagar pelo aluguel é: R${:.2f}' .format(total))