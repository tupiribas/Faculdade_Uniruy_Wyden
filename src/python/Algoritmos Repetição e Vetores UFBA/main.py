'''Arquivo principal de modularização de funcionalidades'''

# from modules.atividade1 import ler_n_numeros_inteiros
# from modules.atividade2 import numero_esta_na_lista
# from modules.atividade3 import (ler_n_numeros_reais,
#                                 mostrar_media,
#                                 mostrar_maior_numero,
#                                 mostrar_menor_numero,
#                                 mostrar_qtd_num_negativos,
#                                 mostrar_qtd_num_positivos)
import os
from modules.atividade4 import (calculo_resjuste_plano_de_saude,
                                vetor_boasvindas)

# Resposta 01)
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

# lista = ler_n_numeros_reais(3)

# Resposta 03)
# Escreva um programa que leia 10 números de reais e informe:
# a) a média dos elementos;
# b) o maior e menor elemento;
# c) a quantidade de elementos positivos e a quantidade de elementos
# negativos.
# print("Média:", mostrar_media(lista))
# print("Maior número:", mostrar_maior_numero(lista))
# print("Menor número:", mostrar_menor_numero(lista))
# print("Quantidade de números positivos:", mostrar_qtd_num_positivos(lista))
# print("Quantidade de números negativos:", mostrar_qtd_num_negativos(lista))

# Resposta 04)
lista_usuarios = []
i = 0

while True:
    try:
        # [Boas vindas]
        vetor_boasvindas('SEJA BEM-VINDO', 50)
        # [Entrada dos dados]
        VALOR_BASE = float(input('Qual valor base de indenização? \n'))
        if VALOR_BASE == -1.0:
            break
        IDADE = int(input('Qual a sua idade? \n'))
        NOME = str(input('Qual o seu nome? \n').title())

        # Limpar terminal para nova
        os.system('cls' if os.name == 'nt' else 'clear')

        # [Processamento e armazenamento dos dados]
        IDENIZACAO = calculo_resjuste_plano_de_saude(VALOR_BASE, IDADE)
        lista_usuarios.append([NOME, IDADE, IDENIZACAO])
    except ValueError:
        # Caso o usuário insira um valor inválido
        print('Digite um número válido.')

for l in enumerate(lista_usuarios):
    print(l)
