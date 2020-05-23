m = '''(DESAFIO 057) Faça um programa que leia o sexo de
    uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso
    esteja errado, peça a digitação novamente até ter um
    valor correto.'''
print(m, '\n')

while True:

    sexo = str(input('Digite seu sexo [M/F]: '))

    if sexo in 'Mm' or sexo in 'Ff':
        
        resultado = 'aceito'

        if sexo in 'Ff':
            print('Aceito! Feminino.')
        
        if sexo in 'Mm':
            print('Aceito! Masculino.')
        
        break
    else:
        resultado = 'negado'
        print('Sexo inválido! Digite outro.')