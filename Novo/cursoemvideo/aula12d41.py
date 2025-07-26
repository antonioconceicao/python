# A Confereção Nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#Até 9 anos: Mirim
# Até 14 anos: Infantil
# Até 19 anos: Junior
# Até 20 anos: Sênior
# Acima: Master

import datetime
ano = int (input('Digite o ano do seu nascimento '))
idade = datetime.date.today().year - ano
print (idade)

if idade <= 9:
    print('Você está na cateogira Mirim')
elif idade <= 14:
    print ('Você está na categoria Infantil')
elif idade <= 19:
    print('Você está na cateogria Junior')
elif idade <= 20:
    print ('Você está na cateogria Sênior')
else:
    print ('Você está na cateogria Master')