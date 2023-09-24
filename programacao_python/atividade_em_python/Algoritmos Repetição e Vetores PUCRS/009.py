'''
Escreva um algoritmo que leia 50 valores e encontre o maior e o menor deles. Mostre o resultado.
'''

menor = 0
for num in range(50):
    numero = input('Digite um número: \n')

    if num == 0:
        menor = numero
    elif numero < menor:
        menor = numero

print(f'O menor número registrado é: {menor}')
    
