#Crie um programa que faça o computador jogar jokenpô com você.


import random
comecar = int (input('Vamos jogar Jokenpo e escolhe uma das opções \n 1 - pedra \n 2- papel  \n 3-tesoura'))
pedra = 1
papel = 2
tesoura = 3


maquina = random.choice([pedra, tesoura, papel])

print (maquina)

if comecar  == maquina:
    print  ('Deu empate! Tenta novamente')
elif (comecar == 1 and maquina == 3) or (comecar == 2 and maquina == 1) or (comecar == 3 and maquina == 2):
    print ('Você ganhou! Da uma nova chance para a maquiona tenta novamente')
else:
    print('Você perdeu! Tenta novamente ')