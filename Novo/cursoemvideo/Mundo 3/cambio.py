#Crie um programa que simule uma operação simples de conversão de moeda.
#O programa deverá receber um valor em reais que o usuário deseja enviar para outro país e calcular quanto ele receberá em uma moeda estrangeira, considerando a cotação atual da moeda escolhida.
#Além da conversão, o programa deverá considerar uma taxa de serviço aplicada pela instituição e informar o valor final recebido pelo usuário.

dolar = 5.14
#spead = 4 /100

print('PW: Câmbio')
print ('O valor do dolar hoje é R$ 5.14')
dinheiro = int( input('Digite o valor que você quer enviar: '))

conta = dinheiro / dolar

print(f'O valor convertido em dolar é U$${conta:.2f}')
