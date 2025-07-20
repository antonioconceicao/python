# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import math
import random

n1 = input ('Digite o nome do primeiro aluno ')
n2 = input ('Digite o segundo nome do aluno ')
n3 = input ('Digite o nome do terceiro aluno ')
n4 = input ('Digite o nome do quarto aluno ')

lista = [n1, n2, n3, n4]

random.shuffle (lista)
print (F'o 1 colocado é {lista[0]} , o 2 colocado é {lista[1]}, o 3 colocado é {lista[2]}, o 4 colocado é {lista[3]} ')


