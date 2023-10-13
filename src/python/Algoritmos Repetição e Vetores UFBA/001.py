'''
Escreva um programa que receba uma lista de 10 inteiros via teclado e
imprima todo a lista em na mesma linha.
'''

lista_numeros = []

for _ in range(10):
    lista_numeros.append(int(input('Digite um número: ')))

print(lista_numeros)
