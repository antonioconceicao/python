#Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequencia de fibonacci.
# Ex: 0 -> 1  -> 1 -> 2 -> 3 -> 5 -> 8
anterior = 0
atual = 1
c= 0
guardardados = []
usuario = int(input('Digite um número para ver a sequencia de fibonacci: '))
sequencia = int (input('Digite quantos números da sequência de Fibonacci você quer ver: '))

while c < sequencia:
    guardardados.append(anterior)
    calculo = anterior + atual
    anterior = atual
    atual = calculo
    c += 1

print('O valores são:', *guardardados)