menor = 0
listadenumeros = [2, 4, 2, 10, 2, 5]

for i, n in enumerate(listadenumeros):
    if i == 0:
        menor = n
    elif menor > n:
        menor = n

print(menor)
