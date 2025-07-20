# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.Faça um programa que ajude ele, lenndo o nome deles e escrevendo o nome do escolhido.
import math
import random

aluno =  input ('Digite o nome do primeiro aluno ')
aluno2 = input('Digite o nome do segundo aluno ')
aluno3 = input('Digite o nome do terceiro aluno ')
aluno4 = input ('Digite o nome do quarto aluno ')


cal = random.choice([aluno, aluno2, aluno3, aluno4])

print (f'O nome escolhido foi {cal}')
