# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
soma_de_notas = 0
for i in range(4):
    soma_de_notas += float(input(f"Digite a {i + 1}ª nota: \n")) # soma de numeros

media = soma_de_notas / 4
print(f"Média: {media:.2f}")
