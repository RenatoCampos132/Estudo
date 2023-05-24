print('-'*15,'Gerador de PA','-'*15)

pri = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))

print('-' * 45)

cont = 1
pa = pri 
termos = 10
tot_termos = 0

while termos > 0:
    while cont <= termos:
        print('{} -> '.format(pa), end = '')

        pa = pa + r
        cont += 1

    print('PAUSA')

    tot_termos = tot_termos + termos 
    cont = 1
    termos = int(input('Quantos termos você quer mostrar a mais: '))

print('\nForam mostrados {} termos'.format(tot_termos))
print('PROGRAMA ENCERRADO')
