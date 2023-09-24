# Solicita ao usuário o valor do lado do quadrado
lado = float(input("Qual o valor do lado do quadrado? "))

# Calcula a area do quadrado
area = lado ** 2

# Calcula o dobro do valor da área do quadrado, calculada anteriormente
dobro_area = 2 * area

# Mostra o resultado
print(f"A área do quadrado é: {area}.")
print(f"O dobro da area do quadrado é: {dobro_area:.2f}.")
