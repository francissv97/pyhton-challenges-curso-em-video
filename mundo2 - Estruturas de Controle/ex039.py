m = ''' (DESAFIO 039)
        Faça um programa que leia o ano de nascimento de
    um jovem e informe, de acordo com sua idade:
        - Se ele ainda vai se alistar ao serviço militar;
        - Se é a hora de se alistar;
        - Se já passou do tempo do alistamento.'''
print(m, '\n')

anoNascimento = int(input('Em que ano você nasceu? '))
dataAtual = 2020
idade = dataAtual - anoNascimento

print(f'\nQuem nasceu em {anoNascimento} tem {idade} anos em {dataAtual}.')

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o alistamento.')
    alistamento = dataAtual + (18 - idade)
    print(f'Seu alistamento será em {alistamento}.')
elif idade > 18:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos.')
    alistamento = dataAtual - (idade - 18)
    print(f'Seu alistamento foi em {alistamento}.')
