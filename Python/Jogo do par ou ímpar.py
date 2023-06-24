from random import randint

print('=-' * 13)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 13)

cont = 0

while True:
    num = int(input('Digite um número: '))
    poi = str(input('Par ou ímpar? [P/I]: ')).strip().upper() [0]

    if poi != 'I' and poi != 'P':
        print('Resposta inválida, tente novamente...')
        print('-' * 40)

    else:
        comnum = randint(0, 10)
        soma = num + comnum

        if soma % 2 == 0: 
            parim = 'P'
            parims = 'PAR'

        elif soma % 2 == 1:
            parim = 'I'
            parims = 'ÍMPAR'

        print('-' * 52)
        print(f'Você jogou {num} e o computador {comnum}. Total deu {soma}, é {parims}')
        print('-' * 52)

        if parim == poi:
            print('VOCÊ VENCEU!!!!')
            cont += 1
            print('Vamos jogar novamente!!')
            print('=-' * 12)

        else:
            print('VOCÊ PERDEU')
            break

print(f'FIM DE JOGO! Você venceu {cont} vezes')
