m = '''(DESAFIO 059) Crie um programa que leia dois valores e mostre
	um menu na tela:
	[1] SOMAR
	[2] MULTIPLICADOR
	[3] MAIOR
	[4] NOVOS NÚMEROS
	[5] SAIR DO PROGRAMA
	Seu programa deverá realizar a operação solicitada em cada caso.'''
print(m, '\n')

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
condicao = int()

while condicao != 5:
	print('''O que deseja fazer com esses números?
		Digite [ 1 ] para SOMA-LOS.
		Digite [ 2 ] para MULTIPLICA-LOS.
		Digite [ 3 ] para SABER QUAL É O MAIOR.
		Digite [ 4 ] para DIGITAR NOVOS NÚMEROS.
		Digite [ 5 ] para SAIR DO PROGRAMA''')

condicao = int(input('Digite: '))