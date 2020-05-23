m = ''' (DESAFIO 015)
    Escreva um programa que pergunte a quantidade de km 
    percorridos por um carro alugado e a quantidade de dias
    pelos quais ele foi alugado. Calcule a preço a pagar, sabendo
    que o carro custa R$60 por dia e R$0.15 por km rodado: '''
print(m, '\n')

dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos km rodados? '))

dias = dias * 60
km = km * 0.15
total = dias + km

print(f'Total a pagar é de R${total:.2f}')
