m = '''(DESAFIO 048)
	Faça um programa que calcule a soma entre todos
	os números ímpares que são multiplos de três e
	que se encontram no intervalo de 1 até 500.'''
print(m, '\n')

contador = int()
somatorio = int()

for i in range(1, 501, 2):
	if i % 3 == 0:
		somatorio += i
		contador += 1

print(f'O somatório dos {contador} valores solicitados é de {somatorio}.')
