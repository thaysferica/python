largura = float(input('largura da parede (m):'))
altura = float (input('altura da parede (m):'))
area = largura * altura
tinta = area / 2 
print(f'sua parede tem a dimensão de {largura}x{altura} e sua area é de {area:2f}m.') 
print (f'para pintar essa parede, voce precisara de {tinta:2f}1 de tinta.')