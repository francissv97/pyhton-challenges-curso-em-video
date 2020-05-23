m = '''(DESAFIO 056)
	Desenvolva um programa que leia o nome, idade e sexo de 4
	pessoas. No final do programa, mostre:
		> A média de idade do grupo;
		> Qual é o nome do homem mais velho;
		> Quantas mulheres têm menos de 20 anos.'''
print(m, '\n')

somatorioIdade = 0

homemVelho = ''
idadeHomemVelho = 0

mulheres20Anos = 0

for i in range(0, 4):

	print('===' * 10)
	print(f'{i + 1}ª PESSOA')
	print('===' * 10)

	nome = str(input(f'Digite o nome da {i + 1}ª pessoa: '))
	nome = nome.capitalize()

	idade = int(input(f'Digite a idade da {i + 1}ª pessoa: '))

	sexo = str(input(f'Digite o sexo da {i + 1}ª pessoa. [F/M]: '))

	somatorioIdade += idade

	if i == 0 and sexo in 'Mm':
		homemVelho = nome
		idadeHomemVelho = idade

	if sexo in 'Mm' and idade > idadeHomemVelho:
		homemVelho = nome
		idadeHomemVelho = idade

	if sexo in 'Ff' and idade < 20:
		mulheres20Anos += 1
print('\n')

mediaIdade = somatorioIdade / 4

print('---' * 15)
print(f'A média de idade do grupo é de {mediaIdade} anos.')
print(f'O homem mais velho tem {idadeHomemVelho} anos e se chama {homemVelho}')
print(f'Total de mulheres com menos de 20 anos: {mulheres20Anos}')
print('---' * 15)
