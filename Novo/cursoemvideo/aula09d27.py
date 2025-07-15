# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Ana Maria de Souza
# primeiro = ana
# último = Souza

nome = input ('Digite o seu nome completo ')
separacao = nome.split()
primeiro = separacao[0]
ultimo = separacao[-1]
print (f'O primeiro nome:{primeiro}\n e o segundo nome: {ultimo}')
