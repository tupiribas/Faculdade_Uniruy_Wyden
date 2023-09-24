# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
from math import pi

raio_do_circulo =  float(input("Qual o raio do círculo (cm) ")) # solicita ao usuáio o raio do círculo
area_do_circulo = pi * raio_do_circulo ** 2

print(f"A área do círculo é aproximadamente ≈ {area_do_circulo:.2f} cm²") # calcula a area do circulo e mostra o resultado
