# Solicita ao usuário a temperatura em fahrenheit
fahrenheit = float(input('Qual a temperatura em fahrenheit? '))

# Calcula e transforma a temperatura em celsius
celsius = 5 * ((fahrenheit - 32) / 9)

# Mostra ao usuário a temperatura convertida
print(f"A temperatura em celsius é: {celsius:.1f} °C")