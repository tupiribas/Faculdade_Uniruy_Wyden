'''
Escrever um algoritmo que leia uma quantidade desconhecida de números e 

1. Conte quantos deles estão nos seguintes intervalos: [0,25], [26,50], [51,75] e [76,100]. 

A entrada de dados deve terminar quando for lido um número negativo.
'''
intervalo1 = 0
intervalo2 = 0
intervalo3 = 0
intervalo4 = 0
while True:
    try:
        numero = int(input('Digite um número: '))

        if 0 < numero <= 25:
            intervalo1+=1
        elif 26 < numero <= 50:
            intervalo2+=1
        elif 51 < numero <= 75:
            intervalo3+=1
        elif 76 < numero <= 100:
            intervalo4+=1

        print(f'Quantidade de números entre 0 e 25: {intervalo1}')
        print(f'Quantidade de números entre 26 e 50: {intervalo2}')
        print(f'Quantidade de números entre 51 e 75: {intervalo3}')
        print(f'Quantidade de números entre 76 e 100: {intervalo4}')
    except ValueError:
        # Caso o usuário insira um valor inválido
        print('Digite um número válido.')
