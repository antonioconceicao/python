#Melhore o jogo do DESAFIO 28 onde o computador vai 'pensar' em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random
maquina = random.randint(1, 10)
guardar = 0
text = -1

while text != maquina:
    text = int (input('Vamos jogar um jogo! Eu vou pensar em número entre 1 e 10 e você precisa dizer qual número eu estou pensando. \n Digite 0 para terminar o jogo \n Digite o número: '))
    guardar += 1

    
    if maquina == text:
        print (f'Parabéns, você acertou e eu estava pensando no {maquina}. Você tentou por {guardar} vezes \n')
    else:
        print (f'Você digitou o número {text}, mas eu não pensei nesse. Você perdeu e tenta de novo!')
print ('------Fim-----')