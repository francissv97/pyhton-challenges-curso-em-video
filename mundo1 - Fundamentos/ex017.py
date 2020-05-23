import math

m = ''' (DESAFIO 017)
	Faça um programa que leia o comprimento do
	cateto oposto e do cateto adjacente de um
	triângulo, calcule e mostre o
	comprimento da hipotenusa: '''
print(m, '\n')

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

hip = math.hypot(co, ca)

print(f'Hipotenusa: {hip}')

''' # Ou...

co = pow(co, 2)
ca = pow(ca, 2)
hi = co + ca
hi = pow(hi, (1/2))

print('A hipotenusa mede {:.2f}'.format(hi)) '''
