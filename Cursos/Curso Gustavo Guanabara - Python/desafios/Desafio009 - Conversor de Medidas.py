# Escreva um program que leia um valor em metros e o exiba convertido em centimetros e meilimetros

print('TABELA DE UNIDADES DE COMPRIMENTO')

metro = float(input('Insira uma distância em metros: '))
km = metro / 1000
hm = metro / 100
dam = metro / 10
dcm = metro * 10
cm = metro * 100
mm = metro * 1000

print('\n km: {} - hm: {} - dam: {} - M: {} - dcm: {} - cm: {} - mm: {}'.format(km, hm, dam, metro, dcm, cm, mm))

input()
