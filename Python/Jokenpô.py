#Programa que joga o classico jogo jokenpô com vc 

from random import randint
from time import sleep

print('''Suas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL 
[ 3 ] TESOURA''')

usuario = int(input('Qual a sua jogada? '))
computador = randint(1, 3) #Gera um número aleatórion entre 1 e 3

print('JO')
sleep(0.7)
print('KEN')
sleep(0.7)
print('PÔ!!!')

#Verifica qual a opção escolhida pelo computador
if computador == 1:
    escolha_comp = 'PEDRA'

elif computador == 2:
    escolha_comp = 'PAPEL'

elif computador == 3:
    escolha_comp = 'TESOURA'

#Verifica qual a opção escolhida pelo usuário
if usuario == 1:
    escolha_usua = 'PEDRA'

elif usuario == 2:
    escolha_usua = 'PAPEL'

elif usuario == 3:
    escolha_usua = 'TESOURA'

else:
    print('Resposta inválida')

#Printa a escolha do computador e do usuário 
print('-=' * 12)
print('''Computador jogou {}
Jogador jogou {}'''.format(escolha_comp, escolha_usua))
print('-=' * 12)

#Verifica e anuncia o vencedor
if usuario == computador:
    print('EMPATE')

elif usuario == 1 and computador == 2:
    print('COMPUTADOR VENCEU')

elif usuario == 2 and computador == 3:
    print('COMPUTADOR VENCEU')

elif usuario == 3 and computador == 1:
    print('COMPUTADOR VENCEU')

elif computador == 1 and usuario == 2:
    print('JOGADOR VENCEU')

elif computador == 2 and usuario == 3:
    print('JOGADOR VENCEU')

elif computador == 3 and usuario == 1:
    print('JOGADOR VENCEU')
