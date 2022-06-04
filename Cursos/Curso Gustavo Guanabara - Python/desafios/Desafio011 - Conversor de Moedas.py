# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.

reais = float(input('Digite a Quantidade de Reais que pretende Converter: '))
dolar = float(0.19)
convert = dolar * reais
print('Você teria U$ = {:.3f} Dolares'.format(convert))
input()
