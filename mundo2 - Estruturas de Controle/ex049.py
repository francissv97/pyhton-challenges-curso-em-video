m = '''(DESAFIO 049)
	Refaça o DESAFIO 009, mostrando a 
	tabuada de um número que que o usuário 
	escolher, só que agora utilizando um laço for.'''
print(m, '\n')

n = int(input('Digite um número: '))

print('==' * 8, f'\n  TABUADA DO {n}')
print('==' * 8)

for i in range(1, 11):
	print(f'| {n} x {i:2} = {n * i:3} |')
