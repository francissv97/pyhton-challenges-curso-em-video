m = ''' (DESAFIO 042)
        Refaça o DESAFIO 035 dos triângulos, acrescentando
    o recurso de mostrar que tipo de triângulo será formado:
        - Equilátero: todos os lados iguais;
        - Isósceles: dois lados iguais;
        - Escaleno: todos os lados diferentes.'''
print(m, '\n')

r1 = float(input('Primeira reta: '))
r2 = float(input('Secunda reta: '))
r3 = float(input('Terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end = '')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓCELES!')
else:
    print('Não é possivel formal um triângulo com essas medidas')