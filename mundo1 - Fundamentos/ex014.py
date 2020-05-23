m = ''' (DESAFIO 014)
    Escreva um programa que converta uma temperatura
    digitada em ºC para ºF: '''
print(m, '\n')

c = float(input('Informe a temperatura em C: '))

f = ((9 * c) / 5) + 32

print(f'A temperatura de {c:.1f} ºC corresponde a {f:.1f} ºF.')
