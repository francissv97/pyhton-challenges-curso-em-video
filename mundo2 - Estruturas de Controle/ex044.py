m = ''' (DESAFIO 044)
        Elabore um programa que calcule o valor a ser pago
    por um produto, considerando seu preço normal e condição
    de pagamento:
        - À vista dinheiro/cheque: 10% de desconto
        - À vista no cartão: 5% de desconto
        - Em até 2x no cartão: preço normal
        - Em 3x ou mais no cartão: 20% de juros'''
print(m, '\n')

print('{:=^40}'.format(' LOJA DO POVO '))

preco = float(input('\nPreço das compras: R$'))

print('---' * 20)
print(' ' * 13, 'FORMAS DE PAGAMENTOS POSSÍVEIS')
print('===' * 20)
print('Digite [ 1 ]: À vista no dinheiro ou cheque. 10% de desconto;')
print('Digite [ 2 ]: À vista no cartão. 5% de desconto;')
print('Digite [ 3 ]: 2x no cartão: Preço normal;')
print('Digite [ 4 ]: 3x ou mais no cartão: 20% de juros.')
print('===' * 20)

condicao = int(input('Qual será a forma de pagamento? Digite a opção desejada: '))
print('---' * 20)

if condicao == 1:
    print('Opção escolhida: À vista no Dinheiro/Cheque, DESCONTO de 10%;')
    novoPreco = preco - (preco * 0.10)
    print(f'Sua compra de R${preco:.2f} vai custar R${novoPreco:.2f} no final.')

elif condicao == 2:
    print('Opção escolhida: À vista no Cartão, DESCONTO de 5%;')
    novoPreco = preco - (preco * 0.05)
    print(f'Sua compra de R${preco:.2f} vai custar R${novoPreco:.2f} no final.')

elif condicao == 3:
    print('Opção escolhida: 2x no Cartão, Preço Normal;')
    print(f'Sua compra vai continuar custando R${preco:.2f}.')

elif condicao == 4:
    print('Opção escolhida: 3x ou mais no Cartão;')
    prestacao = int(input('Quantas parcelas? '))
    novoPreco = preco + (preco * 0.20)
    precoParc = novoPreco / prestacao
    print(f'Sua compra será parcelada em {prestacao}X de {precoParc:.2f} COM JUROS.')
    print(f'Sua compra de R${preco:.2f} vai custar R${novoPreco:.2f} no final.')

else:
    print('Opção inválida, Tente novamente.')