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


def mostrar_media(listadenumeros: list[float]) -> float:
    '''
    03) Escreva um programa que leia 10 números de reais e informe:
        a) a média dos elementos;

    Retorna a media do conjunto de numeros da lista.
    '''
    return sum(listadenumeros) / len(listadenumeros)


def mostrar_maior_numero(listadenumeros: list) -> float:
    '''
    03) Escreva um programa que leia 10 números de reais e informe:
        b) o maior e menor elemento;

    Retorna o maior elemento da lista passada por parâmetro
    '''
    return max(listadenumeros)


def mostrar_menor_numero(listadenumeros: list) -> float:
    '''
    03) Escreva um programa que leia 10 números de reais e informe:
        b) o maior e menor elemento;

    Retorna o maior elemento da lista passada por parâmetro
    '''
    menor = 0
    for i, n in enumerate(listadenumeros):
        if i == 0:
            menor = n
        elif menor > n:
            menor = n
    return menor


def mostrar_qtd_num_positivos(listadenumeros: list) -> int:
    '''
    03) Escreva um programa que leia 10 números de reais e informe:
        c) a quantidade de elementos positivos e a quantidade de elementos
        negativos.

    Retorna o maior elemento da lista passada por parâmetro
    '''
    qtd_num = 0
    for n in listadenumeros:
        if n > 0:
            qtd_num += 1
    return qtd_num


def mostrar_qtd_num_negativos(listadenumeros: list) -> int:
    '''
    03) Escreva um programa que leia 10 números de reais e informe:
        c) a quantidade de elementos positivos e a quantidade de elementos
        negativos.

    Retorna o maior elemento da lista passada por parâmetro
    '''
    qtd_num = 0
    for n in listadenumeros:
        if n < 0:
            qtd_num += 1
    return qtd_num
