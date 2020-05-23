m = ''' (DESAFIO 037)
        Escreva um programa que leia um número inteiro
    qualquer e peça para o usuário escolher qual será a
    base de conversão:
        - 1 para binário;
        - 2 para octal;
        - 3 para hexadecimal.'''
print(m, '\n')

num = int(input('Digite um número: '))

binario = bin(num) [2:]
octal = oct(num) [2:]
hexadecimal = hex(num) [2:]

print(f'''Deseja converter o número {num} para qual base numérica?
    
    Digite [ 1 ] para BINARIO
    Digite [ 2 ] para OCTAL
    Digite [ 3 ] para HEXADECIMAL
''')

opcao = int(input('Digite a opção desejada: '))

if opcao == 1:
    print(f'O número {num} convertido para BINÁRIO é {binario}')
elif opcao == 2:
    print(f'O número {num} convertido para OCTAL é {octal}')
elif opcao == 3:
    print(f'O número {num} Convertido para HEXADECIMAL é {hexadecimal}')
else:
    print('Opção inválida. Tente novamente.')
