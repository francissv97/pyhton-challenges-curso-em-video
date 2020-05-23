m = ''' (DESAFIO 039v2)
    Refaça o DESAFIO 039, mais agora lendo
    o sexo da pessoa, se for uma mulher exiba
    uma mensagem dizendo que não é obrigatório
    o alistamento.'''
print(m, '\n')

sexo = str(input('Antes de tudo, qual é o seu sexo? [F/M]: '))
resp = ''

if sexo in 'Ff':
    print('No Brasil, não é obrigatório o alistamento de mulheres.')
    resp = str(input('Mesmo assim, gostaria de ver sua situação? [S/N]: '))

if sexo in 'Ff' and resp in 'Ss' or sexo in 'Mm':
    anoNascimento = int(input('\nEm que ano você nasceu? '))
    dataAtual = 2020
    idade = dataAtual - anoNascimento

    print(f'\nQuem nasceu em {anoNascimento} tem {idade} anos em {dataAtual}.')

    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade < 18:
        saldo = 18 - idade
        print(f'Ainda faltam {saldo} anos para o seu alistamento.')
        alistamento = dataAtual + (18 - idade)
        print(f'Seu alistamento será em {alistamento}.')
    elif idade > 18:
        saldo = idade - 18
        print(f'Você já deveria ter se alistado há {saldo} anos.')
        alistamento = dataAtual - (idade - 18)
        print(f'Seu alistamento foi em {alistamento}.')
else:
    print('Desculpe, não entendi o que você quis dizer, tente novamente.')