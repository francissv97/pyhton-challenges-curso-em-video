from datetime import date

m = ''' (DESAIO 041)
        A Confederação Nacional de Natação precisa de um
    programa que leia o ano de nascimento de um atleta e
    mostre sua categoria, de acordo com a idade:
        - Até 9 anos: MIRIM;
        - Até 14 anos: INFANTIL;
        - Até 19 anos: JUNIOR;
        - Até 25 anos: SÊNIOR;
        - Acima: MASTER.'''
print(m, '\n')

anoNasc = int(input('Ano de nascimento: '))
dataAtual = date.today().year
idade = dataAtual - anoNasc

print(f'\nO atleta tem {idade} anos.')
if idade <= 9:
    print('Classificação: MIRIM.')
elif idade > 9 and idade <= 14:
    print('Classificação: INFANTIL.')
elif idade > 14 and idade <= 19:
    print('Classificação: JUNIOR.')
elif idade > 19 and idade <= 25:
    print('Classificação: SÊNIOR.')
elif idade > 25:
    print('Classificação: MASTER.')
print()
