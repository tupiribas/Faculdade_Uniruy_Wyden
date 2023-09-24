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

soma = 0.0
cont_salario = 0
cont_num_filho = 0
maior_salario = 0.0
percentual = 0.0
i = 0
while True:
    try:
        salario = float(input('Qual o valor da sua renda mensal? '))
        
        if salario < 0: 
            break
        else: 
            soma += salario
            # Percentual de salários menores que 100
            if salario <= 100.0:
                print('e menor que 100')
                cont_salario += 1

        # Maior salario
        if salario > maior_salario:
            maior_salario = salario
        
        num_filhos = int(input('Quantos filhos você tem? '))

        if num_filhos < 0: # Não conta com idade negativa errados 
            print('A quantidade de filhos está incorreta.')
        else: cont_num_filho += num_filhos

        i += 1
    except ValueError: # Caso o usuário insira uma letra
        print('Digite um valor váido \n')

media_salarial = soma / i
media_num_filhos = cont_num_filho / i
percentual_salario = (cont_salario / i) * 100

print(f'''
Média de salários: R${media_salarial:.2f}
Média do números de filhos: {media_num_filhos} 
Maior salário: {maior_salario}
Percentual de salários menores que R$100.00: {percentual_salario:.0f}%
Programa finalizado.
''')
