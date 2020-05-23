m = ''' (DESAFIO 038)
        Escreva um programa que que leia dois números e 
    compare-os, mostrando na tela uma mensagem:
        - O primeiro valor é maior;
        - O segundo valor é maior;
        - Não existe valor maior, os dois são iguais.'''
print(m, '\n')

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

if n1 > n2:
    print('\nO PRIMEIRO valor é maior.')
elif n2 > n1:
    print('\nO SEGUNDO valor é maior.')
else:
    print('\nNão existe valor maior, o dois são IGUAIS.')