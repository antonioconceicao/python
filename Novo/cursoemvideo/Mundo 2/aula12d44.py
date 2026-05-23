#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#à vista dinheiro/cheque: 10% de desconto
#à vista no cartão: 5% de desconto
#em até 2x no cartão: preço normal
#3x ou mais no cartão: 20% de juros


valor = float (input('Digite o preço do produto R$'))
pagar = int (input('Escolha uma opção para o pagamento \n 1- à vista dinheiro/cheque: 10% de desconto \n 2- à vista no cartão: 5% de desconto \n 3- em até 2x no cartão: preço normal \n 4- 3x ou mais no cartão: 20% de juros '))

desconto10 = valor * (10/100)
desconto5 = valor * (5/100)
cartao2 = valor /2
cartao3 = valor * 0.20

vista = valor - desconto10
vistacartao = valor - desconto5
vistacartao3 = valor + cartao3



if pagar == 1:
    print (f'O novo preço do produto com 10% de desconto é R${vista:.2f}')
elif pagar == 2:
    print (f'O novo preço do produto com 5% de desconto é R${vistacartao:.2f}')
elif pagar == 3:
    print (f'As parcelas em 2x sem Juros fica em R${cartao2:.2f}')
else:
    print(f'As parcelas em 3x com Juros fica em R${vistacartao3:.2f}')
