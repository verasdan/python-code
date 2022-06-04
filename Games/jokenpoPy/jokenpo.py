from random import randint
from time import sleep

lista = ("Pedra", "Papel", "Tesoura")

computador = randint(0,2)

jogador = int(input(
'''Escolha uma opcao para se jogar: 

[0] Pedra
[1] Papel
[2] Tesoura

Digite sua escolha: '''))

print('\n')
print("Preparados?\n")
print("JO\n")
sleep(1)
print("KEN\n")
sleep(1)
print("POOOOOOOH!!!\n")

print("-"*20)
print("Você escolheu: {}".format(lista[jogador]))
print("O seu adversário escolheu: {}".format(lista[computador]))
print("-"*20)
print('\n')

if computador == 0:
    if jogador == 0:
        print("Empate!")

    elif jogador == 1:
        print("Você perdeu")

    elif jogador == 2:
        print("O seu adversário venceu")

    else:
        print("Operação invalida")

elif computador == 1:
    if jogador == 0:
        print("O seu adversário perdeu")

    elif jogador == 1:
        print("Empate!")

    elif jogador == 2:
        print("Você venceu")

    else:
        print("Operação invalida")

elif computador == 2:
    if jogador == 0:
        print("Você venceu")
    elif jogador == 1:
        print("O seu adversário venceu")
    elif jogador == 2:
        print("Empate!")
    else:
        print("Operação invalida")
else:
    print("Operação invalida")

input()