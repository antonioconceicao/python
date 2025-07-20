# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

text = int (input('Vamos jogar um jogo! Eu vou pensar em número entre 0 e 5 e você precisa dizer qual número eu estou pensando '))


if text == 5:
    print ('Você digitou o número 5, mas eu não pensei nesse. Você perdeu e tenta de novo!')

elif text == 4:
    print('Você digitou o número 4, mas eu não pensei nesse. Você perdeu e tenta de novo! ')

elif text == 3:
    print('Você digitou o número 3, mas eu não pensei nesse. Você perdeu e tenta de novo!')

elif text == 2:
    print('Parabéns, você acertou e eu estava pensando no 2. Vamos jogar de novo')
elif text == 1:
    print ('Você digitou o número 1, mas eu não pensei nesse. Você perdeu e tenta de novo!')
else:
    print ('Você digitou o número 0, mas eu não pensei nesse. Você perdeu e tenta de novo!')



