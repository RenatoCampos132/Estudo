from random import randint
from time import sleep

print("-=" * 28)
print("Vou pensar em um numero entre 0 e 5 , tente adivinhar")
print("-=" * 28)

num = randint(0, 5)

chute = int(input("Em que numero eu pensei:"))

print("PROCESSANDO...")
sleep(2)

if chute == num:
    print("Parabens! Você conseguiu me vencer!")
else:
    print("Ganhei! Eu pensei no numero {} e não no {}".format(num, chute))