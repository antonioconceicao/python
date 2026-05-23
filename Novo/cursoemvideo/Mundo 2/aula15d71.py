#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado(número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# obs: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.
cedulas = [50, 20, 10, 1]
somar50 = 0
somar20 = 0
somar10 = 0
somar1 = 0
resto = 0
print('Banco Phoenix Wright')
while True:
    sacar = int (input('Qual valor você quer sacar? R$ '))

    somar50 = sacar // 50
    resto = sacar % 50
    somar20 = resto // 20
    resto = resto % 20
    somar10 = resto // 10
    resto = resto % 10
    somar1 = resto // 1

    break

print(f'Total de cedulas {somar50} de R$ 50')
print(f'Total de cedulas {somar20} de R$ 20')
print(f'Total de cedulas {somar10} de R$ 10')
print(f'Total de cedulas {somar1} de R$ 1')
