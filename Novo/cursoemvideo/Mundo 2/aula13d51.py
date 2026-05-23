#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
# PA = pROGRESSÃO ARITMETICA

primeiro = int (input('Digite o primeiro termo '))
razao = int (input('Digite a razão '))

for conta in range (1, 11):
    pa = primeiro + (conta -1) * razao
    print (pa)
