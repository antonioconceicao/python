#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

valor = int (input('Digite qual tabuada você quer saber '))
for tabuada in range(1, 11):
    n2 = valor * tabuada
    print (f'{valor} x {tabuada} = {n2}')