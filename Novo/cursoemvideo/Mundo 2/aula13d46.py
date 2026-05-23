#Faça um programa que mostre na tela uma contagem repressiva para o estouro de fogos de artifício, indo de 10 até 0,  com uma pausa de 1 segundo entre eles.
import time

print ('Vamos começar a contagem regressiva para estourar os fogos!!!')

for c in range(10, -1, -1):
    print(c)
    time.sleep(1)
print ('Feliz ano novo!')
