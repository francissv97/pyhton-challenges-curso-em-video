m = ''' (DESAFIO 007)
    Desenvolva um programa que leia as duas notas 
    de um aluno, calcule e mostre a sua média: '''
print(m, '\n')

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua secunda nota: '))

media = (n1 + n2) / 2

print(f'A média entre {n1:.1f} e {n2:.1f} igual a {media:.1f}')
