#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

primeiro = float (input('Digite o primeiro segmento '))
segundo =  float (input('Digite o segundo segmento '))
terceiro = float (input('Digite o terceiro segmento '))

conta = abs(segundo - terceiro) < primeiro < segundo + terceiro
conta2 = abs(primeiro - terceiro )< segundo < primeiro + terceiro
conta3 = abs(primeiro - segundo) < terceiro < primeiro + segundo 


print (f'O valor é {conta}, {conta2}, {conta3}')

if conta and conta2 and conta3:
    print ('Esse valor consegue transformar em um triângulo')
else:
    print ('Esses valores não podem formar um triângulo')