'''
Escrever um algoritmo que leia um número n que indica quantos valores devem ser lidos a seguir. 

Para cada número lido, mostre uma tabela contendo o valor lido e o
fatorial deste valor.
'''

f = 10

print(f'{f}! =', end=' ')
for i in range(f, 0, -1):
    if i != 1:
        print(f'{i} x ', end='')
    else:
        print('1 ', end='')
    f *= i
print(f'= {f}')
