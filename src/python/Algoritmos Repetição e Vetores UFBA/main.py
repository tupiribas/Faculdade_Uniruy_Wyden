'''Arquivo principal de modularização de funcionalidades'''

def ler_n_numeros_inteiros(limite: int = 10) -> list[int]:
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


def numero_esta_na_lista(listadenumeros: list[int], numero:int) -> bool:
    '''
    02) Escreva um programa que receba uma listade de 10 inteiros via teclado, em
    seguida o programa deve solicitar um número e informar se o número
    também está na lista ou não.

    Verifica se o número pertence a lista informada. Retorna True ou False.
    '''
    return numero in listadenumeros


# lista = ler_n_numeros_inteiros(3)

# Resposta 02)
# print(lista)

# Resposta 02)
# try:
#     numero_escolhido = int(input('Digite um número: '))
#     print('Resposta 02)')
#     if numero_esta_na_lista(listadenumeros=lista, numero=numero_escolhido) is False:
#         print(f'O número {numero_escolhido} NÃO PERTENCE a lista')
#     else:
#         print(f'O número {numero_escolhido} PERTENCE a lista')
# except ValueError:
#     print('Digite um valor válido!')
