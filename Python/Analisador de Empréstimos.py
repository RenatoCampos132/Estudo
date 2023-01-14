
#Recebe os valores
valor_emprestimo = float(input('Valor do empréstimo: R$'))

salario = float(input('Salário do comprador: R$')) / 100 * 30

anos = int(input('Anos de financiamento:'))

prestacoes = valor_emprestimo / (anos * 12)

#Mostra uma mensagem com as informações
print('Para pagar um empréstimo de R${:.2f} em {} anos, a prestação será de R${:.2f}.'.format(valor_emprestimo, anos, prestacoes))

#Verifica se o valor das prestações ultrapassa o valor de 30% do salário do comprador e mostra se o empréstimo foi aprovado ou não
if prestacoes <= salario:
	print('Empréstimo aprovado, agora sofra para pagar.')

else:
	print('Empréstimo negado, você é muito pobre para pagar isso.')
