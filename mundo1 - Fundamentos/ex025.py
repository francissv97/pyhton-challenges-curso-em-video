m = ''' (DESAFIO 025)
    Crie um programa que leia o nome
    de uma pessoa e diga se ela tem
    "SILVA" no nome: '''
print(m, '\n')

nome = str(input('Digite seu nome completo: '))

nome = nome.strip().upper()

print(f'Seu nome tem Silva? {"SILVA" in nome}')
