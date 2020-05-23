m = ''' (DESAFIO 031)
    Desenvolva um programa que pergunte a distância de
    uma viajem em Km. Calcule o preço da passagem, cobrando
    R$0.50 por km para viajens de até 200km e R$0.45 para
    viajens mais longas.'''
print(m, '\n')

viajem = float(input('Qual a distância da viajem? (em Km) '))

if viajem <= 200:
    viajem = viajem * 0.50
    print('Preço: R$0.50/km')
else:
    viajem = viajem * 0.45
    print('Preço: R$0.45/km')

print(f'Sua passagem vai custar R${viajem:.2f}')
