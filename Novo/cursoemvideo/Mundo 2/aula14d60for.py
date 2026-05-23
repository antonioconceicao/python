#Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Ex: 5 = 5x4x3x2x1 = 120

valor = int (input('Digite um número para ver a fatorial: '))
resultado = 1
for c in range (1,valor+1):
    resultado *= c
print (f'O valor do fatorial do {valor} é {resultado}')