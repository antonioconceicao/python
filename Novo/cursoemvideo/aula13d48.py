#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
sooma = 0
cont = 0
for numero in range(1, 501, 2):
    if numero % 3 == 0 :
        sooma = sooma + numero
        cont = cont + 1
print (f'A soma de todos {cont} total é {sooma}')