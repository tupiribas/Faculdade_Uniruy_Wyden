'''
    Escrever um algoritmo que lê um valor N inteiro e positivo e
    que calcula e escreve o valor de E.

    E = 1 + 1 / 1! + 1 / 2! + 1 / 3! + 1 / N!
'''
try:
    n = int(input('Digite um número \n'))

    if n < 0: print('O valor inserido não é váido.')
    else:
        f = 1
        e = 1.0
        for i in range(1, n + 1):
            f *= i
            termo = 1.0 / f
            e += termo
        print(f'O valor de E = {e}')

except ValueError:
    print('O valor inserido não é um número. Insira um número na próxima!')
finally:
    print('\nFinalizando o sistema... \nFinalizado.')