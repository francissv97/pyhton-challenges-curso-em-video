m = ''' (DESAFIO 035)
    Desenvolva um programa que leia o
    comprimento de três retas e diga ao
    usuário se elas podem ou não formar
    um triângulo.'''
print(m, '\n')

r1 = float(input('Primeira reta: '))
r2 = float(input('Secunda reta: '))
r3 = float(input('Terceira reta: '))

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print(True)
else:
    print(False)
