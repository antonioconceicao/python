#Escreva um programa para aprovar o emprestimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float (input('Qual é o valor da imóvel? '))
salario = float (input('Digite o seu salário R$'))
tempo = int (input('Quantos anos você quer pagar o imóvel '))

meses = tempo * 12
emprestimo = casa / meses
limite = salario * 0.3

if emprestimo >  limite:
    print ('Infelizmente o financiamento foi negado. A parcela mensal ultrapassa os 30% ')
else:
    print (f'Parabéns, você consegue financiar esse imóvel. As parcelas mensais são R${emprestimo:.2f} e você vai pagar por {tempo} anos') 
