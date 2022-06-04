a = input('Digite algo: ')

print('O tipo primitivo desse valor é', type(a))
print('Contém espaços? ', a.isspace)
print('É um número? ', a.isnumeric())
print('É alfabeto? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Esta em maiúsculo? ', a.isupper())
print('Esta em minúscula? ', a.islower())
print('Esta capitalizada? ', a.istitle())

input()
