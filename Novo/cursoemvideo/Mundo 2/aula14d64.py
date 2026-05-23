#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles.(Desconsiderando o flag).

numeros = 0
quantidade = 0


print ('Bem-vindo! Começa a usar o nosso programa! \n para encerrar o programa digite 999')

while True:
    digitar = int (input('Digite um valor: '))

    if digitar == 999:
        fim = input(f'Você digitou 999 e o programa vai ser encerrado! \n Você digitou {quantidade} números. \n A conta total dos números digitado foi: {numeros}  ')
        break
    numeros += digitar
    quantidade += 1
    
    