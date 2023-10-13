'''
Chico tem 1,50 metro e cresce 2 centímetros por ano, 
enquanto Zé tem 1,10 metro e cresce 3 centímetros por ano.

Construa um algoritmo que calcule e imprima quantos
anos serão necessários para que Zé seja maior que Chico.
'''

altura_chico = 150
altura_ze = 110
taxa_cresce_chico = 2
taxa_cresce_ze = 3

anos = 0
while altura_ze <= altura_chico:
    altura_chico += taxa_cresce_chico
    altura_ze += taxa_cresce_ze
    anos += 1

print(f"Levará {anos} anos para Zé ter a mesma altura de Chico")