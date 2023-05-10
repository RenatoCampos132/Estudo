from time import sleep

run = True

pri = float(input('Primeiro valor: '))
seg = float(input('Segundo valor: '))

while run == True:
    print('-' * 25)
    print('''    [1] Somar
    [2] Multiplicar
    [3] Dividir
    [4] Maior
    [5] Números novos
    [6] Sair do programa''')
    print('-' * 25)
    opção = int(input('>>>Qual sua opção: '))

    if opção == 1:
        print('A soma entre {} e {} é igual a {}'.format(pri, seg, pri + seg))
        
    elif opção == 2:
        print('A multiplicação de {} por {} é igual a {}'.format(pri, seg, pri * seg))

    elif opção == 3:
            print('A divisão entre {} e {} é igual a {}'.format(pri, seg, pri / seg))

    elif opção == 4:
        if pri > seg:
            print('Entre {} e {} o maior é {}'.format(pri, seg, pri))

        else:
            print('Entre {} e {} o maior é {}'.format(pri, seg, seg))

    
        
    elif opção == 5:
        print('Informe os números novamente')
        sleep(1)
        pri = float(input('Primeiro valor: '))
        seg = float(input('Segundo valor: '))
        sleep(1)

    elif opção == 6:
        print('Finalizando...')
        run = False
        
    else:
        print('Opção inválida, tente novamente')

    sleep(2)

print('\nPrograma encerrado')
