m = ''' (DESAFIO 010)
    Crie um programa que leia quanto uma pessoa 
    tem na carteira e mostre quantos Dólares ela 
    pode comprar: '''
print(m, '\n')

real = float(input('Quanto você tem na carteira? R$ '))
dolar = real / 5.73

print(f'Com R${real} na carteira é possivel comprar US${dolar:.2f}')
