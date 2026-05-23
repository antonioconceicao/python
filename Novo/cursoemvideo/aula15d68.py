#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random
par = 'p'
impar = 'i'
vitoria = 0

print('Vamos jogar Par ou Ímpar')

while True:
    numero = int (input('Digite um valor: '))
    escolha = input ('Par ou ímpar [P/I] ')
    minuscula = escolha.lower()


    maquina = random.randint(0, 10)
    soma = numero + maquina


    if soma % 2 == 0:
        print (f'Você jogou {numero} e o computador {maquina}. Total deu {soma}. É um número PAR. ')
    else:
        print (f'Você jogou {numero} e o computador {maquina}. Total deu {soma}. É um número ÍMPAR. ')
    if (minuscula  == par) and (soma % 2 == 0) or (minuscula == impar) and (soma % 2 == 1):
        print('Você ganhou! \n Vamos jogar novamente!')
        vitoria += 1

    else:
        print(f'Você perdeu! \n Game over \n Você ganhou {vitoria}')
        break