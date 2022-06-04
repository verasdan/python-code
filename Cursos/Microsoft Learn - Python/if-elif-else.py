# Há três partes na instrução if:

# A palavra-chave if
# A expressão booliana value == '7'
# O caractere dois-pontos : necessário

value = int(input('Digite um número: '))
    
if value == '7':
    print('O valor é 7')
elif value == '8':
    print('O valor é 8')
else:
    print('O valor não é o que esta procurando!')
    
print('Pronto!!')

input()
