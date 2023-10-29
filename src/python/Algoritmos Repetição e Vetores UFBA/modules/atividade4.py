'''sada'''


def vetor_boasvindas(titulo: str, espacamento=25):
    '''
    Função para padronizar a apresentação inicial do sistema

    arguments:
        titulo : str
        espacamento : int - default: 25
    return none
    '''
    print('-'*espacamento)
    print(titulo.title().center(espacamento))
    print('-'*espacamento)


def percentual(valor: float) -> float:
    '''
    arguments:
        valor : float

    Retorna o calculo percentual do valor passado pelo argumento : float
    '''
    return valor / 100


def calculo_resjuste_plano_de_saude(valor_base: float, idade_pasciente: int) -> float:
    '''
    Retorna o reajuste de indenização sobre o valor base de acordo 
    com a idade do paciente.

    arguments:
        valor_base : float
        idade_pasciente : int

    return idenizacao : float
    '''
    idenizacao = 0.0
    if idade_pasciente <= 12:
        idenizacao = valor_base * percentual(30)
    elif 13 <= idade_pasciente <= 49:
        idenizacao = valor_base * percentual(10)
    elif 50 <= idade_pasciente < 65:
        idenizacao = valor_base * percentual(15)
    else:
        idenizacao = valor_base * percentual(35)
    return idenizacao
