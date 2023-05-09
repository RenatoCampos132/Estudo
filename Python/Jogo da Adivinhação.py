from random import randint 
from  time import sleep

print('Sou seu computador...')

num = randint(0, 10)

print('Acabei de pensar em um número entre 0 e 10.')
print('Será que voçê consegue adivinhar qual foi?')
sleep(2)

pal = int(input('Qual o seu palpite: '))
cont = 1

while pal != num:
    if pal > num:
        pal = int(input(('Menos... Tente mais uma vez: ')))

    elif pal < num:
        pal = int(input('Mais... Tente mais uma vez: '))

    cont += 1

print('Acertou com {} tentativas. Parabéns'. format(cont))
