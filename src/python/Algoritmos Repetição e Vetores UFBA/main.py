'''Arquivo principal de modularização de funcionalidades'''


def ler_n_numeros_inteiros(limite:int=10) -> list[int]:
    '''
    01) Escreva um programa que receba uma lista de 10 inteiros via teclado e
    imprima todo a lista em na mesma linha.

    Captura uma quantidade delimitada de numeros inteiros e retorna uma lista feita,
    caso contrário, retorna uma lista vazia.

    default: limite [int]
    '''
    try:
        return [int(input('Digite um número: ')) for _ in range(limite)]

    except ValueError:
        print('Ops! Esse valor não é válido.')
        return []

print("Resposta 01)\n", ler_n_numeros_inteiros(10))
