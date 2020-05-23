m = ''' (DESAFIO 036)
        Escreva um programa para aprovar o empréstimo
    bancário para a compra de uma casa. O programa vai 
    perguntar o valor da casa, o sálario do comprador
    e em quantos anos ele vai pagar.
        Calcule o valor da prestação mensal, sabendo que ela
    não pode exceder 30% do salário ou então o empréstimo
    será negado.'''
print(m, '\n')

casa = float(input('Valor da casa: R$'))
salario = float(input('Salário: '))
financiamento = int(input('Quantos anos de financiamento? '))

prestacao = casa / (financiamento * 12)
salario30por100 = salario * 0.30

print(f'\nPara pagar uma casa de R${casa:.2f} em {financiamento} ', end = '')
print(f'anos a prestação será de R${prestacao:.2f}')
print(f'\n30% do seu salário equivale a R${salario30por100:.2f}')

if prestacao > salario30por100:
    print('\nOu seja, empréstimo NEGADO!')
    print(f'A prestação excedeu 30% do seu salário.')
else:
    print('\nOu seja, o empréstimo pode ser CONCEDIDO!')
    print(f'A prestação NÃO excedeu 30% do seu salário.')
