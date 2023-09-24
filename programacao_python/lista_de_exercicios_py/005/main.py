# Faça um Programa que converta metros para centímetros.
print("Converter de metros para centímetros: \n")
metros = float(input("Quantos métros (m)?")) # pede o usuário a medida em metros

centimetros = float(metros * 100)
print(f"{metros:.2f} m x {centimetros:.2f} cm") # calcula e mostra na tela
