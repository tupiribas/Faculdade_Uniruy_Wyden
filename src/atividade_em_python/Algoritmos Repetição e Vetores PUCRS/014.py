'''
Escrever um algoritmo que leia um número não determinado de valores.

* calcule a média aritmética dos valores lidos, 
* a quantidade de valores positivos, 
* a quantidade de valores negativos;
* o percentual de valores negativos e positivos. 

Mostre os resultados.
'''

numeros = []
while True:
    try:
        numeros.append(int(input('Digite um número: ')))

        # Media
        SOMA = 0
        for n in numeros:
            SOMA += n
        media = SOMA/(len(numeros))

        # Quantidade de valores positivos e negativos
        QUANTIDADE_POSITIVO = 0
        QUANTIDADE_NEGATIVO = 0
        MAIOR = 0
        MENOR = 0
        for n in numeros:
            MENOR = 0
            if n > 0:
                QUANTIDADE_POSITIVO += 1
            elif n < 0:
                QUANTIDADE_NEGATIVO += 1
            

        # Percentual positivo e negativo
        percent_positivo_negativo = ((MAIOR - MENOR) / MENOR) * 100

        print(
            f'Média aritmética {media:.2f}\nQuantidade de valores positivos {QUANTIDADE_POSITIVO}\nQuantidade de valores negativos {QUANTIDADE_NEGATIVO}\nPercentual de valores negativos e positivos {percent_positivo_negativo}%')
    except ValueError:
        # Caso o usuário insira um valor inválido
        print('Digite um número válido.')
