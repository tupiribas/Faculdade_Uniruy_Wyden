'''
Escreva um algoritmo que calcule a média aritmética das
3 notas dos alunos de uma classe. O algoritmo deverá ler, 
além das notas, o código do aluno e deverá ser
encerrado quando o código for igual a zero.
'''
# Sem Vetor

total_avaliacoes = 0.0
total_notas = 0.0
quantidade_alunos = 1

while True:
    try:
        codigo = int(input(f'\nVocê é o {quantidade_alunos}º aluno. \nDigite seu código: \n'))

        if codigo <= 0: break # Caso insira o código 0

        for avaliacao in range(3):
            nota = float(input(f'Quanto você tirou na {avaliacao+1}ª avaliação? \n'))
            total_avaliacoes += nota

        total_notas += total_avaliacoes
        quantidade_alunos += 1
    except ValueError:
        # Caso o usuário insira um valor inválido
        print('Digite um número válido.')

if codigo < 0:
    print('Número negativo não é valido! \n')
else:
    media = total_notas / quantidade_alunos
    print(f'A média aritimetica dessa classe é: {media:.2f}')
