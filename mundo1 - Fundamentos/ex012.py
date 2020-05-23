m = ''' (DESAFiO 012)
	Faça um algoritmo que leia o preço de um produto e 
	mostre seu preço, com 5% de desconto: '''
print(m, '\n')

num = float(input('Qual é o preço do produto? R$'))

desconto = num * 0.05
valorFinal = num - desconto

print(f'Desconto de R${desconto:.2f}')
print(f'O produto que custava R${num:.2f}, na promoção com desconto de 5% vai custar R${valorFinal:.2f}')
