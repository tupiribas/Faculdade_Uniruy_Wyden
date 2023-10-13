'''
Faça um programa que encontre a probabilidade de se obter um número par em um
lançamento de um dado.
'''
lados_totais = int(input('Informe o total de lados de um dado: '))
SOMA_PARES = 0
SOMA = 0

for l in range(1, lados_totais+1):
    if l % 2 == 0:
        SOMA_PARES += 1
    SOMA += 1

probabilidade_um_dado = SOMA_PARES / SOMA

print(f'A probabilidade de cairem numeros pares por lançamento de um dado: {probabilidade_um_dado}')
