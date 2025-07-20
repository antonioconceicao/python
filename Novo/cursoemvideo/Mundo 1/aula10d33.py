#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

import math
num = int (input('Digite um número '))
num2 = int (input('Digite o segundo número '))
num3 = int (input('Digite o terceiro número '))

maior = max(num, num2, num3)
minimo = min (num, num2, num3)

print(f'O maior número é {maior} e o menor número é {minimo}')