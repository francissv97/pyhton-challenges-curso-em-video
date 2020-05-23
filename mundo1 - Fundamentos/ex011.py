m = ''' (DESAFIO 011)
    Faça um programa que leia a largura e a altura de uma parede em
    metros, calcule a sua área e a quantidade de tinta necessária para
    pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²: '''
print(m, '\n')

largura = float(input('Qual a largura da parede(em m)? '))
altura = float(input('Qual a altura da parede(em m)? '))

area = altura * largura
tinta = area / 2

print(f'Esta parede tem dimensões de {largura}x{altura}, sua área é de {area:.2f}m².')
print(f'É será necessário {tinta:.2f}l de tinta para pinta-la.')
