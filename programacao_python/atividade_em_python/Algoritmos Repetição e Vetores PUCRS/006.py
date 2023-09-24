'''
Em uma eleição presidencial existem quatro candidatos. 
Os votos são informados através de códigos. 
Os dados utilizados para a contagem dos votos obedecem à seguinte codificação:
- 1,2,3,4 = voto para os respectivos candidatos;
- 5 = voto nulo;
- 6 = voto em branco;

Elabore um algoritmo que leia o código do candidado em um voto. Calcule e escreva:
- total de votos para cada candidato;
- total de votos nulos;
- total de votos em branco;
Como finalizador do conjunto de votos, tem-se o valor 0.
'''

total_votos = 0
total_votos_nulos = 0
total_votos_brancos = 0

try:
    while True:
        voto = int(input('[1] - Tupi Guedes\n[2] - Lula\n[3] - Maurício Freitas\n[4] - Juninho Laércio\n[5] - Nulo\n[6] - Branco\n[0] - Para sair\nDigite um número para votar: \n'))
        
        if voto <= 0:
            break
        if voto == 5:
            total_votos_nulos += 1
        elif voto == 6:
            total_votos_brancos += 1

        total_votos += 1
except ValueError:
    # Caso o usuário insira um valor inválido
    print('\nDigite um número válido.\n')


if voto < 0:
    print('Número negativo não é valido! \n')
else:
    print(f'Total de votos para cada candidato: {total_votos}\nTotal de votos nulos: {total_votos_nulos}\nTotal de votos em branco: {total_votos_brancos}')