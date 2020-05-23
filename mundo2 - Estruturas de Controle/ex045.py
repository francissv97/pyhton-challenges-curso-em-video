from random import choice
from time import sleep

m = ''' (DESAFIO 045)
        Crie um programa que faça o computador
    jogar jokenpô com você:'''
print(m)

while True:
    
    jokenpo = ['Pedra', 'Papel', 'Tesoura']

    # 0 = ENCERRAR, 1 = Pedra, 2 = Papel e 3 Tesoura
    print('==' * 20)
    print('\nOpções de Jogadas:')
    print('Digite [ 0 ]: ENCERRAR')
    print('Digite [ 1 ]: PEDRA')
    print('Digite [ 2 ]: PAPEL')
    print('Digite [ 3 ]: TESOURA')
    jogada = int(input('Agora é Sua Vez: '))

    if jogada == 0:
        print('~~' * 15)
        print('Jogo Encerrado, Até Mais!')
        print('~~' * 15)
        break

    jokenpo = choice(jokenpo)
    print('JO..')
    sleep(0.5)
    print('KEN..')
    sleep(0.5)
    print('PO!!\n')

    print('--' * 20)

    ######################################
    if jogada == 1 and jokenpo == 'Pedra':
        print('Você jogou PEDRA e eu TAMBÉM joguei PEDRA.')
        print('Deu EMPATE!')
    elif jogada == 1 and jokenpo == 'Papel':
        print('Você jogou PEDRA e eu joguei PAPEL.')
        print('Você PERDEU!')
    elif jogada == 1 and jokenpo == 'Tesoura':
        print('Você jogou PEDRA e eu joguei TESOURA.')
        print('Você GANHOU!')

    ########################################
    elif jogada == 2 and jokenpo == 'Pedra':
        print('Você jogou PAPEL e eu joguei PEDRA.')
        print('Você GANHOU!')
    elif jogada == 2 and jokenpo == 'Papel':
        print('Você jogou PAPEL e eu TAMBÉM joguei PAPEL.')
        print('Deu EMPATE!')
    elif jogada == 2 and jokenpo == 'Tesoura':
        print('Você jogou PAPEL e eu joguei TESOURA.')
        print('Você PERDEU!')
    
    ########################################
    elif jogada == 3 and jokenpo == 'Pedra':
        print('Você jogou TESOURA e eu joguei PEDRA.')
        print('Você PERDEU!')
    elif jogada == 3 and jokenpo == 'Papel':
        print('Você jogou TESOURA e eu joguei PAPEL.')
        print('Você GANHOU!')
    elif jogada ==  3 and jokenpo == 'Tesoura':
        print('Você jogou TESOURA e eu TAMBÉM joguei TESOURA.')
        print('Deu EMPATE!')
    print('--' * 20)
