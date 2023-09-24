'''
    Escrever um algoritmo que lê 5 valores para a, um de cada vez, 
    e conta quantos destes valores são negativos, escrevendo esta informação.
'''

contator = 0
for i in range(5):
    a = int(input('Digite um número \n'))
    if a < 0:
        contator+=1

print(f'Total de números de negativos: {contator}')
