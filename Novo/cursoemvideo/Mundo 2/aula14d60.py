#Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Ex: 5 = 5x4x3x2x1 = 120

import math
import time
valor = int (input('Digite um número para ver a fatorial: '))
r = 1
contador = valor

while contador > 1:
    r *= contador
    contador -= 1
    time.sleep(0.1)

print (f'O fatorial de {valor} é {r}')
