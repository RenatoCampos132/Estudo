mais18 = homi = mm20 = cont = 0

print('=-' * 20)
print('CADASTRADOR DE PESSOAS')
print('=-' * 20)

while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper() [0]

    while sexo != 'F' and sexo != 'M':
        print('Resposta inválida, tente novamente!')
        sexo = str(input('Sexo [M/F]: ')).strip().upper() [0]

    cont += 1

    if  idade > 18:
        mais18 += 1

    if sexo == 'M':
        homi += 1

    if sexo == 'F' and idade < 20:
        mm20 += 1

    run = str(input('Castrar mais uma pessoa? [S/N]: ')).strip().upper() [0]
    print('-' * 40)

    while run != 'S' and run != 'N':
        print('Resposta inválida, tente novamente!')
        run = str(input('Castrar mais uma pessoa? [S/N]: ')).strip().upper() [0]
        print('-' * 40)

    if run == 'N':
        break
    

print(f'Foram cadastradas um total de {cont} pessoas\nAo todo temos {homi} homens cadastrados\nE temos {mm20} mulheres com menos de 20 anos')
