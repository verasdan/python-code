largura = float(input('Largura da parede em Metros(m): '))
altura = float(input('Altura da parede em Metros(m): '))
tintaNecessaria = (altura * largura)/2**2
print('Altura = {:.2f}\nLargura = {:.2f}\nLitros Necessários: {} l(Litros)'.format(altura, largura, tintaNecessaria))

input()