'''
Escrever um algoritmo que leia 20 valores para uma variável n e, para cada um deles, calcule a tabuada de 1 até n. 
Mostre a tabuada na forma:
1 x n = n
2 x n = 2n
3 x n = 3n
.......
n x n = n2
'''

numero = int(input('Digite um número: \n'))

print(f'Tabuada do {numero}')
for n in range(20+1):
    print(f'{n} x {numero} = {n*numero}')
