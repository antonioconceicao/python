#Faça um programa que leia o peso de cinco pessoas.No final, mostre qual foi o maior e o menor peso lidos.
peso = []
for verificador in range(1, 6):
    pessoas = float (input (f'Digite o {verificador} peso da pessoa. Digite apenas números inteiros '))
    peso.append(pessoas)
minimo = min(peso)
maximo = max(peso)
print(f'O maior peso é {maximo} e o menor é {minimo}')