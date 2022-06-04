# Ramificar a execução do código com base na entrada do usuário

valor = input('Would you like to continue? (y/n) : ')

if valor == 'y' or valor == 'yes':
    print('Continuando ...')
    
elif valor == 'n' or valor == 'no':
    print('Saindo...')
    
else:
    print('Por favor tente responder com yes ou no.')

input()