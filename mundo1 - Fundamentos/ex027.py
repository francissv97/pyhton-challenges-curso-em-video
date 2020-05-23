m = ''' (DESAFIO 027)
    Faça um programa que leia o nome completo
    de uma pessoa, mostrando em seguida o primeiro
    e o último nome separadamente:
        Ex: Ana Maria de Souza
        Primeiro: Ana
        Último: Souza.'''
print(m, '\n')

nome = str(input('Digite seu nome completo: '))

nome = nome.strip().title().split()

primeiro = nome[0]

ultimo = nome[len(nome) -1]

print('Olá, muito prazer!')
print(f'Seu primeiro nome é {primeiro}.')
print(f'e seu último nome é {ultimo}.')
