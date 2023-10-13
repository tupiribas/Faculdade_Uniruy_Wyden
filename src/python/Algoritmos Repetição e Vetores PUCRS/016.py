'''
Escrever um algoritmo que lê um conjunto não determinado de valores, um de cada vez.

Escreve uma tabela com cabeçalho, que deve ser repetido a cada 20 linhas. A
tabela conterá o valor lido, seu quadrado, seu cubo e sua raiz quadrada.
'''

def mostrar_resultado(titulo: str='Cabeçalho'):
    '''Mostrar o resultado dos calculos em formato de tabela
    titulo : str - default : "Cabeçalho"'''
    print('-'*40)
    print(' '*15, end=' ')
    print(titulo)
    print('-'*40)

def calcular_quadrado(valor: float=0.0):
    '''Calcula o valor e o eleva ao quadrado (x²)
    valor : float - default : 0.0'''
    valor_ao_quadrado = valor ** 2
    return valor_ao_quadrado


def calcular_cubo(valor: float=0.0):
    '''Calcula o valor e o eleva ao cubo (x³)
    valor : float - default : 0.0'''
    valor_ao_cubo = valor ** 3
    return valor_ao_cubo


def calcular_raiz_quadrada(valor: float=0.0):
    '''Calcula o valor e o eleva a raiz quadrada
    valor : float - default : 0.0'''
    for i in range(5):
        ...


linhas = 0
while True:
    try:
        if linhas == 20:
            mostrar_resultado('Resultado')
        linhas+=1
    except ValueError:
        # Caso o usuário insira um valor inválido
        print('Digite um número válido.')
