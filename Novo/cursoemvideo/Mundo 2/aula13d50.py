#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.Se o valor digitado for ímpar, desconsidere-o

cont = 0
soma = 0
for numero in range (1, 7):
    valor = int (input(f'Digite o {numero} valor: '))
    if valor % 2 == 0:
        soma += numero
        cont += 1
print(f'Você informou {cont} números PARES e a soma foi {soma}')
        