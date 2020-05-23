from time import sleep

m = ''' (DESAFIO 029)
    Escreva um programa que leia a velocidade de
    um carro. Se ele ultrapassar 80km/h, mostre uma
    mensagem dizendo que ele foi multado. A multa vai
    custar R$7.00 por cada Km acima do limite: '''
print(m, '\n')

velocidade = float(input('Qual a velocidade do veículo? '))

if velocidade > 80:
    print('VELOCIDADE EXEDIDA!')

    multa = (velocidade - 80) * 7
    print('CALCULANDO multa, aguarde...')
    sleep(2)

    print(f'Você será multado em R${multa:.2f}')
else:
    print('Tudo ok, velocidade dentro do limite.')

print('Tenha um bom dia, até mais')
