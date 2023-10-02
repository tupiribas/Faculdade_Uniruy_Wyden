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
        SOMA_POSITIVO = 0
        SOMA_NEGATIVO = 0
        for n in numeros:
            MENOR = 0
            if n > 0:
                SOMA_POSITIVO += 1
            elif n < 0:
                SOMA_NEGATIVO += 1

        # Percentual positivo e negativo
        percent_negativos = (SOMA_NEGATIVO / len(numeros)) * 100
        percent_positivos = (SOMA_POSITIVO / len(numeros)) * 100

        print(f'Média aritmética {media:.2f}\nQuantidade de valores positivos {SOMA_POSITIVO}\nQuantidade de valores negativos: {SOMA_NEGATIVO}\nPercentual de valores negativos: {percent_negativos:.2f}% \nPercentual de valores positivos: {percent_positivos:.2f}%\n')
    except ValueError:
        # Caso o usuário insira um valor inválido
        print('Digite um número válido.')
