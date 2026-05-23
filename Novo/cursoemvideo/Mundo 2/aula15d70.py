#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
#a - Qual é o total gasto na compra.
#b - Quantos produtos custam mais de R$1000.
#c - Qual é o nome do produto mais barato.

total = 0
maisdemil = 0
nomedobarato = ""
maisbarato = 0

print ('Loja do Phoenix Wright')

while True:
    produto = input ('Nome do produto: ')
    preco = int (input('Preço: R$ '))
    continuar = input('Quer continuar? [S/N]').lower()
    while continuar not in "sn":
        continuar = input('Você não digitou corretamente. Digite S/N ').lower()
    total += preco
    if maisbarato == 0:
        maisbarato = preco
        nomedobarato = produto
    if preco > 1000:
        maisdemil += 1
    if preco < maisbarato:
        maisbarato = preco
        nomedobarato = produto 
    if continuar == 'n':
        break

print ('OBJECTION! Obrigado pelas compras e volte sempre!')
print (F'O total da compra foi R$ {total}')
print (f'Temos {maisdemil} produtos custando mais de R$1.000')
print (f'O produto mais barato foi {nomedobarato} que custa R$ {maisbarato} ')
    



