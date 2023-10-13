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

def ler_n_numeros_reais(limite: int = 10) -> list[float]:
    '''
    03) Escreva um programa que receba uma lista de 10 reais via teclado e
    imprima todo a lista em na mesma linha.

    Captura uma quantidade delimitada de numeros reais e retorna uma lista feita,
    caso contrário, retorna uma lista vazia.

    default: limite [int]
    '''
    try:
        return [float(input('Digite um número: ')) for _ in range(limite)]

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

def mostrar_media_reais(listadenumeros: list[float]) -> float:
    '''
    Escreva um programa que leia 10 números de reais e informe:
        a) a média dos elementos;

    Retorna a media do conjunto de numeros da lista.
    '''
    return sum(listadenumeros) / len(listadenumeros)

def mostrar_maior_numero(listadenumeros: list):
    '''
    03) Escreva um programa que leia 10 números de reais e informe:
        b) o maior e menor elemento;

    Retorna o maior elemento da lista passada por parâmetro
    '''
    return max(listadenumeros)

# lista = ler_n_numeros_inteiros(10)

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

lista = ler_n_numeros_reais(10)

# Escreva um programa que leia 10 números de reais e informe:
# a) a média dos elementos;
# b) o maior e menor elemento;
# c) a quantidade de elementos positivos e a quantidade de elementos
# negativos.
print(mostrar_media_reais(lista))
print(mostrar_maior_numero(lista))
