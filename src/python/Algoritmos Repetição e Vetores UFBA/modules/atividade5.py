'''
. Escreva um programa que leia três vetores do mesmo tamanho (N) e:
a) calcule a norma de cada um dos vetores, informe qual vetor tem a maior
norma1
;
b) calcule o vetor soma dos três vetores2
'''
from math import sqrt


def transforma_listas_to_dicionario(listas: list, *chaves: str) -> dict:
    '''Transforma listas em um único dicionário. \n
        Obtendo um conjunto de listas de elementos e as futuras respectivas chaves(nomes).

        arguments:
            listas: list, *chaves: str
        return novo_dicionario : dict'''
    if len(listas) != len(chaves):  # Caso tenha erro nos parâmetros
        print('A quantidade de listas ou de arguentos tem que ser igual! Observe os tamanhos: ',
              len(listas), len(chaves))
    novo_dicionario = {}
    for i, chaves in enumerate(chaves):
        novo_dicionario[chaves] = listas[i]
    return novo_dicionario


def __raiz_quadrada(valor: float) -> float:
    '''Retorna a raiz quadrada de um determinado valor passado como argumento.

    arguments:
        valor : int ou float'''
    return sqrt(valor)


def soma_elementos_lista(lista: list[int]) -> int:
    '''
    Retorna a soma dos elementos de uma única lista.

    arguments:
        lista : list[int]
    return soma : int
    '''
    soma = 0
    for n in lista:
        soma += n
    return soma


def mostrar_maior_vetor(dicionario: dict[str, int]) -> list:
    '''Imprime a chave e o valor, com maior valor do dicionario.

    arguments:
        listas : dict[str, int]
    return : list'''
    novo_dicionario = {}
    for k, v in dicionario.items():
        # Calcula a soma e raiz quadrada de cada elemento em uma nova lista
        novo_dicionario[k] = __raiz_quadrada(soma_elementos_lista(v))
    return max(novo_dicionario.items(), key=lambda x: x[1])
