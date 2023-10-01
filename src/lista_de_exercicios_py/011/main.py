# Solicita dois números ao usuário
num1 = int(input("Digite o 1ª valor: "))
num2 = int(input("Digite o 1ª valor: "))
# Especialidade esse aqui tem que ser real
num3 = float(input("Digite o 3ª valor: "))

# O produto do dobro do primeiro com metade do segundo
resultado_a = (2 * num1) * (num2 / 2)

# A soma do triplo do primeiro com o terceiro.
resultado_b = 3 * num1 + num3

# O terceiro elevado ao cubo.
resultado_c = num3 ** 3

# Exibe os resultados
print("a. O produto do dobro do primeiro com metade do segundo é:", resultado_a)
print("b. A soma do triplo do primeiro com o terceiro é:", resultado_b)
print("c. O terceiro elevado ao cubo é:", resultado_c)
