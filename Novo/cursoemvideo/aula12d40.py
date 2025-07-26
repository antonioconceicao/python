#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: Reprovado
# Média entre 5.0 e 6.9: Recuperação
# Média 7.0 ou superior: Aprovado

nota = float (input('Digite a sua primeira nota '))
nota2 = float (input('Digite a sua segunda nota '))

media = (nota + nota2) / 2

if media >= 7.0:
    print (f'Você foi aprovado! Sua media é {media}')
elif media >= 5.0 and  media <= 6.9:
    print ('Você está em recuperação!')
else:
    print ('Você foi reprovado')