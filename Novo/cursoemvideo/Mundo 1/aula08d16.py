#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

#Ex: Digite um número: 6.127
#o número 6.127 tem a parte inteira 6.


import math
text = float (input ('Digite um número '))
n1 = math.floor(text)
print (f'O número {text} tem a parte inteira {n1}')