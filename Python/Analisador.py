soma = 0
homi_mais_velho = ''
homi_idade = 0
menores = 0

for p in range(1, 5):
        print('-'*15, '{}ª PESSOA'.format(p), '-'*15)
        nome = str(input('Nome: ')).strip()
        idade = int(input('Idade: '))
        sexo = str(input('Sexo [F/M]: ')).strip()

        soma = soma + idade

        if sexo == 'M' and idade > homi_idade:
                homi_mais_velho = nome
                homi_idade = idade

        if sexo == 'F' and idade < 20:
                menores = menores + 1


print('\nA média de idade do grupo é de {:.2f} anos'.format(soma / 4))
print('O homem mais velho tem {} anos e se chama {}'.format(homi_idade, homi_mais_velho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(menores))
