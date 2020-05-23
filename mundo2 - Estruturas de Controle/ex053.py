m = ''' (DESAFIO 053)
	Crie um programa que leia uma frase qualquer e 
	diga se ela é um palíndromo, desconsidere os espaços.
		Ex: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA
			O LOBO AMA O LOBO, ANOTARAM A DATA DA MARATONA'''
print(m)

frase = str(input('Digite qualquer frase: '))

frase = frase.upper()

fraseSemEspacos = frase.replace(' ', '')

fraseInvertida = ''

for i in range(len(fraseSemEspacos), 0, -1):

	fraseInvertida += fraseSemEspacos[i - len(fraseSemEspacos) - 1]

print(f'A frase "{frase}" invertida e sem espaços é igual a "{fraseInvertida}"')

if fraseSemEspacos == fraseInvertida:
	print('Ou seja, temos um PALINDROMO!')
else:
	print('São diferentes, nada de palindromo aqui.')
