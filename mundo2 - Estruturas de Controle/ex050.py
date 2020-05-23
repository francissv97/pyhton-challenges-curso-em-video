m = '''(DESAFIO 050)
	Desenvolva um programa que leia seis números
	inteiros e mostre a soma apenas daqueles que 
	forem pares. Se o valor for ímpar, desconsidere-o.'''
print(m, '\n')

soma = 0

for i in range(0, 6):
	n = int(input(f'Digite o {i + 1}º número: '))
	if n % 2 == 0:
		soma += n

if soma == 0:
	print('Nenhum número par foi digitado')
else:
	print(f'A soma de todos os números pares digitados foi de {soma}.')
