'''
Escreva um algoritmo que leia um número n (número de termos de uma progressão aritmética),

a1 ( o primeiro termo da progressão) e r (a razão da progressão) e
escreva os n termos desta progressão, bem como a soma dos elementos.
'''

N = 10
A1 = 26
R = 5

AN = A1

for a in range(A1, (A1+(N-1)*R)+1, R):
    print(a, end=' ')
