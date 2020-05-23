m = ''' (DESAFIO 004)
    Faça um programa que leia algo pelo teclado e
    mostre na tela o seu primitivo e todas as informações
    possiveis sobre ela: '''
print(m, '\n')

n = input('Digite algo: ')

print(f'O tipo é {type(n)}')
print(f'Só tem espaços? {n.isspace()}')
print(f'É numérico? {n.isnumeric()}')
print(f'É alfanumérico? {n.isalnum()}')
print(f'É alfabético? {n.isalpha()}')
print(f'É minusculo? {n.islower()}')
print(f'É maiusculo? {n.isupper()}')
print(f'É Capitalizado? {n.istitle()}')
print(f'É decimal? {n.isdecimal()}')
