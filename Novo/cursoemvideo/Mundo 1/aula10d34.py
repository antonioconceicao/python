#Escreva programa que pergunte o salário de um funcionario e calcule o valor do seu aumento.
#Para salários superiores a R$ 1.250, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.

salario = float (input('Digite o seu salario e descubra o valor do aumento R$ '))

superior = salario * 0.10
inferior = salario  * 0.15
sresul = salario + superior
iresul = salario + inferior

if salario > 1250:
    print (f'O novo salario incluido o 10% de aumento é {sresul}')
else:
    print (f'O novo salario incluido o 15% de aumento é {iresul}')

