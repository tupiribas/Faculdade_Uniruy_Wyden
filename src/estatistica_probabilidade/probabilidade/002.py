'''
Faça um programa que mostre o espaço amostral se jogássemos,
ao mesmo tempo, 2, 3 ou mais dados.
'''

for i in range(1, 6):
    for j in range(1, 6):
        for a in range(1, 6):
            print(f'({i}, {j}, {a})')

