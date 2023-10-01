'''
Construir um algoritmo que calcule a média aritmética de vários 
valores inteiros positivos, lidos externamente. 

O final da leitura acontecerá quando for lido um valor negativo.
'''

soma_valores_internos = 0
quantidade_valores_internos = 0
valores_internos = 0

while True:
    try:
        valores_internos = int(input('Digite um número: \n'))

        if valores_internos < 0:
            # Fechar programa
            break

        quantidade_valores_internos += 1
        soma_valores_internos += valores_internos
    except ValueError:
        # Caso o usuário insira um valor inválido
        print('Digite um número válido.')

media_aritimetica = soma_valores_internos / quantidade_valores_internos
print(f'A média aritimétrica desses números: {media_aritimetica}')