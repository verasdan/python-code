import random

value = random.randint(1, 10)
count = 0
guess = 0
while guess != value:
    count += 1
    guess = input('Digite um número entre 1 e 10: ')
    if guess.isnumeric():
        guess = int(guess)
else:
    print(f'Você acertou! Foram {count} tentativas!')

input()