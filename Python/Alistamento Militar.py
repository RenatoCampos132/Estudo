#Script para a saber o ano que se deve alistar no exército

import datetime

genero = input('Qual o seu gênero M/F:')

#Verifica o gênero do usuario
if genero == 'F': 
    print('O alistemento militar não é obrigatorio para mulheres')

else:
    ano_nasc = int(input('Qual o ano de nascimento:'))

    ano_atual = datetime.date.today().year #Pega o ano atual
    idade = ano_atual - ano_nasc

    print('Quem nasceu em {} tem {} em {}'.format(ano_nasc, idade, ano_atual))
    
    #Verifica se o usuario tem mais, menos ou 18 anos e printa o quanto falta ou o quanto já passou da data de se alistar
    if idade < 18:
        print('Ainda faltam {} anos para o alistamento'.format(18 - idade))
        print('Seu alistamento será em {}'.format(ano_atual + (18 - idade)))

    elif idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!!')

    elif idade > 18:
        print('Você já deveria ter se alistado á {} anos'.format(ano_atual - (ano_nasc + 18)))
        print('Seu alistamento foi em {}'.format(ano_nasc + 18))
