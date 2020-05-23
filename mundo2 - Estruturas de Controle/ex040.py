m = ''' (DESAFIO 040)
        Crie um programa que leia duas notas de um aluno e 
    calcule sua média, mostrando uma mensagem no final, de
    com a média atingida:
        - Média abaixo de 5.0: REPROVADO;
        - Média entre 5.0 e 6.9: RECUPERAÇÃO;
        - Média 7.0 ou superior: APROVADO.'''
print(m, '\n')

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if nota1 > 10 or nota2 > 10 or nota1 < 0 or nota2 < 0:
    print('Nota(s) inválida(s), tente novamente.')
else:
    print(f'\nCom as notas {nota1} e {nota2}, sua MÉDIA será de {media}.\n')
    if media < 5:
        print('O aluno foi REPROVADO.') 
    elif media >= 5 and media < 7: # if 7 > media >= 5, essa sintaxe tem o mesmo resultado. 
        print('O aluno ficou de RECUPERAÇÃO.')
    elif media >= 7:
        print('O aluno foi APROVADO!')