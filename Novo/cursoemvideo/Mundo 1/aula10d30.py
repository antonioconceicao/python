#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int (input('Digite um número para saber se ele é par ou ímpar '))
par = numero % 2


if par == 0:
    print ('Esse número é par')
else:
    print('Esse é numero impar')