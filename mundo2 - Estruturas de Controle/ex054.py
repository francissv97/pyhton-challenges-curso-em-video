m = '''(DESAFIO 054)
	Crie um programa que leia o ano de nascimento 
	de sete pessoas. No final, mostre quantas pessoas 
	ainda não atingiram a maioridade e quantas já são maiores.'''
print(m)

data = 2020
maiores = 0
menores = 0

for i in range(0, 7):
	n = int(input(f'Ano de nascimento da {i + 1}ª pessoa: '))
	if data - n >= 18:
		maiores += 1
	else:
		menores += 1

print(f'Pessoas que já alcançaram a maioridade: {maiores}.')
print(f'Pessoas que ainda NÃO alcançaram a maioridade: {menores}.')