#Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.

valor = float (input('Digite a distância e descubra o valor da viagem'))


cent = valor * 0.50
longo = valor * 0.45


if valor <= 200:
    print (f'Sua viagem de {valor} km custará R$ {cent}')
else:
    print (f'Sua viagem de {valor} km custará R$ {longo}')