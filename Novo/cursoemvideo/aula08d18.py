#Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.
import math

angulo = float (input('Qual o número do angulo? '))


angulo2 = math.radians (angulo)
seno2 = math.sin(angulo2)
cosseno2 = math.cos(angulo2)
tangente2 = math.tan(angulo2)

print (f'O valor do seno é {seno2 :.4f}, do cosseno {cosseno2 :.4f}, e tangente é {tangente2 :.4f} ')
