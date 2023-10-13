'''
Escreva um algoritmo que leia o código de um aluno e suas três notas. 

* Calcule a média ponderada do aluno, considerando que o 
peso para a maior nota seja 4 e para as duas restantes, 3. 

Mensagens a serem mostradas
* Mostre o código do aluno
* Mostrar suas três notas
* Mostrar a média calculada
* Mostrar a mensagem "APROVADO" se a média for maior ou igual a 5 e "REPROVADO" se a
média for menor que 5. 

Repita a operação até que o código lido seja negativo.
'''

while True:
    try:
        codigo = int(input('Digite seu código: \n'))

        if codigo < 0:
            print('Finalizando sistema...')
            break  # Caso insira o código 0 ou errado

        notas = []  # Reinicializar lista de notas
        MEDIA = 0.0

        for avaliacao in range(3):
            notas.append(
                float(input(f'Quanto você tirou na {avaliacao+1}ª avaliação? \n')))

        for n in notas:
            if n != max(notas):
                MEDIA += n * 3
            else:
                MEDIA += n * 4

        MEDIA /= 10

        print(f'Código do aluno {codigo} \nNotas: {notas}\nMédia: {MEDIA:.1f}')
        if MEDIA >= 5:
            print('APROVADO')
        else:
            print('REPROVADO')
    except ValueError:
        # Caso o usuário insira um valor inválido
        print('Digite um número válido.')

print('Finalizado')
