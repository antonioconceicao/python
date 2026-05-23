#Crie um programa que leia vários números  inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)


valor = 0
contador = 0


while True:
    numero = int (input('Digite um valor: '))
    
    if numero == 999:
        print ('O programa vai ser encerrado!')
        break
    valor += numero
    contador += 1



print (f'O total dos valores é {valor}. Você digitou {contador} números ')