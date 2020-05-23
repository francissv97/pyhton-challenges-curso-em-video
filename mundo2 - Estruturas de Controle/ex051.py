m = '''(DESAFIO 051)
	Desenvolva um programa que leia o primeiro
	termo e a razão de uma PA. No final, mostre 
	os dez primeiros termos dessa progressão.'''
print(m, '\n')

print('====' * 5, '\n10 TERMOS DE UMA PA')
print('====' * 5)

primeiro = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))

for contador in range(0, 10):
	print(primeiro, '>', end = ' ')
	primeiro += razao
print('ACABOU')
