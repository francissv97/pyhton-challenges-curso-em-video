m = '''(DESAFIO 055)
	Faça um programa que leia o peso de cinco 
	pessoas, mostre qual foi o maior e o menor pelo lidos.'''
print(m)

maior = float()
menor = float()

for contador in range(0, 5):

	print('=' * 19)
	print(f'==== {contador + 1}ª PESSOA ====')
	
	peso = float(input('Peso: '))

	if contador == 0:
		maior = peso
		menor = peso

	if peso > maior:
		maior = peso

	if peso < menor:
		menor = peso

	print(f'Maior peso atualmente: {maior}Kg')
	print(f'Menor peso atualmente: {menor}Kg\n')

print(f'Maior peso do grupo: {maior}Kg')
print(f'Menor peso do grupo: {menor}Kg')
