# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
# Digite um número: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

numero =  (input('Digite um número '))
ms = int(numero) # eu tive que converter string para int para funcionar o código e estava dando erro se eu não fizesse isso


mu = ms % 10
mz = (ms // 10) % 10
mc = (ms // 100) % 10
mm = (ms // 1000) % 10

print(f'{'Milhar:':>2} {numero[0]}')
print (f'{'Centena:':>2} {numero[1]}')
print (f'{'Dezena:' :>2}{ numero[2]}')
print (f'{'Unidade:':>2}{ numero[3]}')

print ('----------- CONTA COM MATEMATICA')

print (f'Unidade: {mu}')
print (f'Dezena: {mz}')
print (f'Centena: {mc}')
print (f'Milhar: {mm}')