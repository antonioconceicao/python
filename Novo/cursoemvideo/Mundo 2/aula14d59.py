#Crie um programa que leia dois valores e mostre um menu na tela:
# 1 somar
# 2 multiplicar
# 3 maior
# 4 novos números
# 5 sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso


comecar = -1
iniciar = 1

valor = int (input('Digite o primeiro valor: '))
valor2= int (input('Digite o segundo valor: '))

while comecar != iniciar:
    menu = int (input('Menu \n Escolha as opções abaixo: \n 1 somar \n 2 multiplicar \n 3 Descubra qual valor é maior ou são iguais \n 4 novos números \n 5 sair do programa \n Você vai escolher o número:  '))
    if menu == 1:
        soma = valor + valor2
        print(f'A soma do {valor} e {valor2} é {soma}')
    elif menu == 2:
        multiplicar = valor * valor2
        print(f'A multiplicação entre {valor} e {valor2} é {multiplicar}')
    elif menu == 3:
        if valor > valor2:
            print (f'O maior valor é {valor}')
        elif valor2 > valor:
            print (f' elif O maior valor é {valor2}')
        else:
            print ('Os valores são iguais')
    elif menu == 4:
        print('Limpando os números e começando novamente')
        valor = int (input('Digite o primeiro valor: '))
        valor2= int (input('Digite o segundo valor: '))
    elif menu == 5:
        print ('Terminando o processos!')
        break
    else:
        print('Número invalido! tenta novamente')
print ('----Saindo do programa-----')
