#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo'

text = input('Digite o nome da cidade e descubra se ela tem Santo ')
divisao = text.split()[0]
pequeno = text.lower()
vdd = 'santo' in pequeno
print (f'Resultado é {vdd}')