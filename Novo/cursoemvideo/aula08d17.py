#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.
import math
text = int(input('Digite o valor do catetos oposto? '))
text2 = int (input('Digite o valor do adjacente? '))

conta = math.hypot(text, text2)
print (f'O comprimento da hipotenusa é {conta :.2f}' )
