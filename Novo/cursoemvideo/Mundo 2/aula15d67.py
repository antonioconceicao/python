#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

calculo = 1

while True:
    tabuada = int (input('Quer ver a tabuada de qual valor? '))

        
    if  tabuada < 0:
        print('Programa encerrado e volte sempre!!') 
        break

    for verifacador in range (1, 11):
        print (f'{tabuada} x {verifacador} = {tabuada*verifacador}')
        



