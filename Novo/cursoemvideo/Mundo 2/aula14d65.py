#Crie um programa que leia vários números inteiros pelo teclado.No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

valores = 0
guardarvalores = []
media = 0

print('Bem-vindo! Obrigado por usar o Tabajara Inc! O programa vai começar agora!\n Para terminar o programa digite a letra 999')

contador = 0

while True :
    sequencia = int(input('Digite um valor: '))
    
    if sequencia == 999:
        print(' O programa foi encerrado! ')
        break
    valores += sequencia
    contador += 1
    guardarvalores.append(sequencia)




media = valores / contador
minimo = min(guardarvalores)
maximo = max(guardarvalores)


print(f'O resultado da media é {media} \n O menor valor é {minimo} \n O maior número é {maximo}')
