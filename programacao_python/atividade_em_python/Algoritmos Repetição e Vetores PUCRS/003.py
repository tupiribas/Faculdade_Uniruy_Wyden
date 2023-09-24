'''
A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, 
coletando dados sobre o salário e número de filhos. A prefeitura deseja saber:

    a) média do salário da população;
    b) média do número de filhos;
    c) maior salário;
    d) percentual de pessoas com salário até R$100,00.
    O final da leitura de dados se dará com a entrada de um salário negativo. (Use o comando ENQUANTO-FAÇA) 
'''

# Fazendo a atividade sem vetor:

print('Pesquisa da Prefeitura de Ruy Barbosa')

total_salario = 0.0
perc_salario_ate_100 = 0
total_filhos = 0
maior_salario = 0.0
percentual = 0.0
quantidade_pessoas = 0
while True:
    try:
        salario = float(input('Qual o valor da sua renda mensal? '))
        
        if salario < 0: # Fecha o programa quando digitado valor negativo em salário
            break

        num_filhos = int(input('Quantos filhos você tem? '))

        total_salario += salario
        quantidade_pessoas += 1

        # Não conta com idade negativa errados 
        if num_filhos > 0:
            total_filhos += num_filhos
        else:
            print('A quantidade de filhos está incorreta.')

        # Obter o percentual de salários menores que 100
        if salario <= 100.0:
            perc_salario_ate_100 += 1

        # Obter o maior salario
        if salario > maior_salario:
            maior_salario = salario
    except ValueError: 
        # Caso o usuário insira um valor inválido
        print('Digite um número válido \n')

media_salarial = total_salario / quantidade_pessoas
media_num_filhos = total_filhos / quantidade_pessoas
perc_salario_ate_100 = (perc_salario_ate_100 / quantidade_pessoas) * 100

print(f'''
Média de salários: R${media_salarial:.2f}
Média do números de filhos: {media_num_filhos} 
Maior salário: {maior_salario}
Percentual de salários menores que R$100.00: {perc_salario_ate_100:.0f}%
Programa finalizado.
''')
