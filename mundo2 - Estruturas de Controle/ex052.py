m = '''(DESAFIO 052)
	Faça um programa que leia um número inteiro
	e diga se ele é ou não um número primo.'''
print(m)

n = int(input('Digite um número: '))

divisivel = 0

for i in range(1, n + 1):
	if n % i == 0:
		divisivel += 1

print(f'Número de divisores para o número {n}: {divisivel}.')

if divisivel == 2:
	print('Por isso, ele É PRIMO.')
else:
	print('Por isso, ele NÃO É PRIMO.')
