n1 = int (input('Quantos dias alugados? '))
n2 = float (input('Quantos Km rodados? '))
preco = n1  * 60
rodado = n2 * 0.15
total =  preco + rodado
print ('O valor que você vai pagar é R$ {:.2f}'.format(total))
