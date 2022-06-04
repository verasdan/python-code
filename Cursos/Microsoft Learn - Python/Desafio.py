# Neste desafio, você criará um contador de calorias que solicita ao usuário:

# A data atual (em qualquer formato)
# Calorias ingeridas no café da manhã
# Calorias ingeridas no almoço
# Calorias ingeridas no jantar
# Calorias ingeridas no lanche

#==========================================================

data = input('Digite a data de hoje: ')
c_cafe = float(input('Calorias ingeridas no café da manhã: '))
c_almoco = float(input('Calorias ingeridas no almoço: '))
c_jantar = float(input('Calorias ingeridas no jantar: '))
c_lanche = float(input('Calorias ingeridas no lanche: '))
c_total = c_cafe + c_almoco + c_jantar + c_lanche

print('As calorias do dia {}, é no total de {}'.format(data, c_total))

input()
