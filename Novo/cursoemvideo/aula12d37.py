#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# -1 para binário
# -2 para octal
# -3 para hexadecimal

numero = int (input('Digite um número '))
decisao = int (input('Escolha a conversão do número \n 1 para binario \n 2 para octal \n 3 hexadecimal '))
binario = bin(numero)
octal = oct(numero)
hexdecimal = hex(numero)


if decisao == 1:
    print(f'O número convertido em binário é {binario[2:]}')
elif decisao == 2:
    print (f'O número convertido em octal é {octal[2:]}')
elif decisao == 3:
    print(f'O número convertido em hexadecimal é {hexdecimal[2:]}')
else:
    print ('O número que você escolheu é invalido e tenta novamente! escolha entre o número 1,2 ou 3.')