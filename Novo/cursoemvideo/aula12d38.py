#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais

numero = int (input ('Digite o primeiro número '))
numero2 = int ( input ('Digite o segundo número '))

if numero > numero2:
    print (f'O  primeiro é maior')
elif numero2 > numero:
    print ('O segundo é maior')
else:
    print ('Não existe valor maior e os dois são iguais')