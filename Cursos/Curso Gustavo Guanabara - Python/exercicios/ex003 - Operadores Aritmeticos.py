# Excercicio 03

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um numero: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {}, o prduto é {} e a divisão é {:.2f}'.format(s, m, d), end=' | ')
print('Divisão inteira é {} e potência é {}'.format(di, e))
