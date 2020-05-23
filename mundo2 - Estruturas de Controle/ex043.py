m = ''' (DESAFIO 043)
        Desenvolva uma lógica que leia o peso e altura de uma
    pessoa. Calcule seu IMC e mostre seu status, de acordo
    com a tabela abaixo:
        - Abaixo de 18.5: Abaixo do peso;
        - Entre 18.5 e 25: Peso ideal;
        - 25 até 30: Sobrepeso;
        - 30 até 40: Obesidade;
        - Acima de 40: Obesidade mórbida.'''
print(m, '\n')

peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))

imc = peso / (altura ** 2)

print(f'O IMC foi de {imc:.2f}')

if imc < 18.5:
    print('Você está abaixo do peso normal, cuide-se.')
elif imc >= 18.5 and imc < 25:
    print('PARABÉNS, você está na faixa de peso ideal.')
elif imc >= 25 and imc < 30:
    print('Você está com Sobrepeso.')
elif imc >= 30 and imc < 40:
    print('Você está com Obesidade.')
elif imc >= 40:
    print('Você está com Obesidade mórbida, cuide-se.')