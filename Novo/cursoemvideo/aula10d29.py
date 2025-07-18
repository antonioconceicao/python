#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$ 7,00 por cada km acima do limite.

valor = float (input('Digite a velocidade do carro '))
multa = 7
limite = 80
preco = (valor - limite) * multa


if valor > limite:
    print(f'Você ultrapassou o limite adequado e a sua multa vai ser R$ {preco}')
else:
    print('Você estava dentro do limite estabelecido.Continue assim!')