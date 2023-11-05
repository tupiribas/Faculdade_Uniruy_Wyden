'''Arquivo principal de modularização de funcionalidades'''

# Resposta 01)
# from modules.atividade1 import ler_n_numeros_inteiros
# Resposta 02)
# from modules.atividade2 import numero_esta_na_lista
# Resposta 03)
# from modules.atividade3 import (ler_n_numeros_reais,
#                                 mostrar_media,
#                                 mostrar_maior_numero,
#                                 mostrar_menor_numero,
#                                 mostrar_qtd_num_negativos,
#                                 mostrar_qtd_num_positivos)
# Resposta 04)
# import os
# from modules.atividade4 import (calculo_resjuste_plano_de_saude,
#                                 vetor_boasvindas)
# Resposta 05)
import modules.atividade5 as actv5


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
# lista_usuarios = []
# i = 0

# while True:
#     try:
#         # [Boas vindas]
#         vetor_boasvindas('SEJA BEM-VINDO', 50)
#         # [Entrada dos dados]
#         VALOR_BASE = float(input('Qual valor base de indenização? \n'))
#         if VALOR_BASE == -1.0:
#             break
#         IDADE = int(input('Qual a sua idade? \n'))
#         NOME = str(input('Qual o seu nome? \n').title())

#         # Limpar terminal para nova
#         os.system('cls' if os.name == 'nt' else 'clear')

#         # [Processamento e armazenamento dos dados]
#         IDENIZACAO = calculo_resjuste_plano_de_saude(VALOR_BASE, IDADE)
#         lista_usuarios.append([NOME, IDADE, IDENIZACAO])
#     except ValueError:
#         # Caso o usuário insira um valor inválido
#         print('Digite um número válido.')

# for l in enumerate(lista_usuarios):
#     print(l)

# Resposta 05)

vetor1 = [5, 2, 4, 5, 6, 7, 8, 3, 54, 5643]
vetor2 = [6, 34, 54, 1, 5, 8, 9, 4, 2, 3]
vetor3 = [6, 3, 2, 8, 4, 9, 3, 4, 43, 12]

# a) A raiz quadrada da soma dos elementos de cada um dos vetores,
# informe qual vetor tem a maior resultado
novo_dicionario = actv5.transforma_listas_to_dicionario(
    [vetor1, vetor2, vetor3], 'Vetor 1', 'Vetor 2', 'Vetor 3')
print('O maior vetor é', actv5.mostrar_maior_vetor(novo_dicionario)[
      0], ' com raiz', actv5.mostrar_maior_vetor(novo_dicionario)[1])
# b) A soma dos elemento dos 3 vetores
print('A soma dos elementos dos 3 vetores: ')
print(actv5.soma_elementos_lista(vetor1))
print(actv5.soma_elementos_lista(vetor2))
print(actv5.soma_elementos_lista(vetor3))
