m = ''' (DESAFIO 022)
    Crie um programa que leia o nome completo
    de um pessoa e mostre:
        > O nome com todas as letras maiúsculas;
        > O nome com todas minusculas;
        > Quantas letras ao todo (sem considerar espaços);
        > Quantas letras tem o primeiro nome. '''
print(m, '\n')

nome = str(input('Digite seu nome completo: ')).strip()

print('Analizando seu nome...')
print(f'Seu nome em maiúsculas: {nome.upper()}.')
print(f'Seu nome em minúsculas: {nome.lower()}.')

semEspaco = nome.replace(' ', '')
print(f'Seu nome tem {len(semEspaco)} letras ao todo (sem contar espaços).')

dividido = nome.split()
print(f'Seu primeiro nome é {dividido[0]} e tem {len(dividido[0])} letras')
