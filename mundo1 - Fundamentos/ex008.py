m = '''(DESAFIO 008)
    Escreva um programa que leia um valor em metros
    e o exibs convertido em centímetros e milimetros: '''
print(m, '\n')

n = float(input('Digite alguma medida(em metros): '))

km = n / 1000
hm = n / 100
dam = n / 10
dm = n * 10
cm = n * 100
mm = n * 1000

print(f'{n}m equivale a \n{km}km \n{hm}hm \n{dam}dam \n{dm}dm \n{cm}cm \n{mm}mm')
