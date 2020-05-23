m = ''' (DESAFIO 034)
    Escreva um programa que pergunte o salário
    de um funcionário e calcule o valor do seu
    aumento. 
    Para salários superiores a R$1.250.00, calcule
    um aumento de 10%.
    Para os inferiores ou iguais, o aumento é de 15%.'''
print(m, '\n')

salario = float(input('Quanto você ganha atualmente? R$'))

if salario > 1250:
    novoSalario = salario + (salario * 0.10)
    print('\nSeu aumento será de 10%.')
    print(f'Você que ganhava R${salario:.2f} vai passar a receber R${novoSalario:.2f}.')
else:
    novoSalario = salario + (salario * 0.15)
    print('\nSeu aumento será de 15%.')
    print(f'Você que ganhava R${salario:.2f} vai passar a receber R${novoSalario:.2f}.')
