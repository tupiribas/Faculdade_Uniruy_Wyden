'''
Escreva um algoritmo que calcule a média dos números digitados pelo usuário, 
se eles forem pares. Termine a leitura se o usuário digitar zero (0).
'''

total_numeros_pares = 0

while True:
    try:
        numero = int(input('Digite um número \n'))

        if numero <= 0:
            break
        elif numero % 2 == 0:
            total_numeros_pares += 1
    except ValueError:
        # Caso o usuário insira um valor inválido
        print('Digite um número válido.')

if numero < 0:
    print('Número negativo não é valido! \n')
else:
    print(f'O total de números pares é {total_numeros_pares}')