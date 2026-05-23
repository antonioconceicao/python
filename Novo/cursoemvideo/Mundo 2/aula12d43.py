#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#Abaixo de 18.5: Abaixo do peso
#Entre 18.5 e 25: Peso ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade mórbida

altura = float (input('Digite a sua altura '))
peso = float (input('Digite a sua peso '))

imc = peso / (altura* altura)

if imc <= 18.5:
    print('Você está abaixo do peso')
elif 18.5 < imc <= 25:
    print ('Você está no peso ideal')
elif 25 < imc <= 30:
    print ('Você está no sobrepeso')
elif  30 < imc <= 40:
    print ('Você está na obesidade')
else:
    print ('Obesidade mórbida')

