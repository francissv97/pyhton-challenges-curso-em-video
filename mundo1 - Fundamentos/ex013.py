m = ''' (DESAFIO 013)
    Faça um algoritmo que leia o salário de 
    um funcionário e mostre seu novo salário, com 15% de aumento: '''
print(m, '\n')

salario = float(input('Qual o salário do funcionário? R$ '))

aumento = salario * 0.15
novoSalario = salario + aumento

print(f'Aumento de R${aumento:.2f}')
print(f'Um funcionário que ganhava R${salario:.2f}, com 15% de aumento, passa a receber R${novoSalario:.2f}')
