# Solicita ao usuário a temperatura em celsius
celsius = float(input('Qual a temperatura em celsius? '))

# Calcula e transforma a temperatura em fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Mostra ao usuário a temperatura convertida
print(f"A temperatura em fahrenheit é: {fahrenheit:.1f} °F")