m = ''' (DESAFIO 006)
    Crie um algoritmo que leia um número e mostre
    seu dobro, triplo e raiz quadrada: '''
print(m, '\n')

n = int(input('Digite um número: '))

d = n * 2
t = n * 3
r = pow(n, (1/2))

print(f'O dobro de {n} é {d}')
print(f'O triplo de {n} é {t}')
print(f'A raiz quadrada de {n} é {r:.2f}')
