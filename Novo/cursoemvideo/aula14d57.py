#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'm' ou 'f'.Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = ['m', 'f']
guardardados = ""
while guardardados not in sexo:
    digitar = input('Digite o seu sexo M para masculino e F para feminino ')
    if digitar.lower() in sexo:
        guardardados = digitar.lower()
        print (f'O seu sexo é {guardardados}.')
    else:
        print('Você digitou errado o seu sexo! Tenta novamente')
print ('-------FIM------')       
