'''
Testes estáticos funcionais
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


def maior_vetor(listas: dict[str, int]) -> str:
    '''Retorna a chave com maior valor do dicionario.
    
    arguments:
        listas : dict[str, int]
    return : str'''
    novo_dicionario = {}
    for k, v in listas.items():
        # Calcula a soma e raiz quadrada de cada elemento em uma nova lista
        novo_dicionario[k] = __raiz_quadrada(soma_elementos_lista(v))
    return max(novo_dicionario, key=novo_dicionario.get)

vetor1 = [5, 2, 4, 5, 6, 7, 8, 3, 57, 5]
vetor2 = [6, 34, 54, 1, 5, 8, 9, 4, 2, 3]
vetor3 = [6, 3, 2, 8, 4, 9, 3, 4, 43, 12]

x = transforma_listas_to_dicionario(
    [vetor1, vetor2, vetor3], 'Vetor 1', 'Vetor 2', 'Vetor 3')
print(type(maior_vetor(x)))
