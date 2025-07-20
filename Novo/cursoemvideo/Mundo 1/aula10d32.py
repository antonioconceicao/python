# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
import calendar
ano = int (input('Digite um ano para saber se o é ano bissexto  '))

data = calendar.isleap(ano)


if data:
    print (f'O ano {ano} é bissexto')
else:
    print (f'O ano {ano} não é bissexto')

