#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.No final do programa, mostre:
#A média de idade do grupo
#Qual é o nome do homem mais velho
#Quantas mulheres têm menos de 20 anos.

nome = []
idade = []
sexo = []

for info in range(1,5):
    print(f'---{info} pessoa-----')
    n = input('Nome:')
    ida = int (input('Idade:'))
    s = input('Sexo [m/f]: ')
    nome.append(n)
    idade.append(ida)
    sexo.append(s)
media = sum (idade) / len(idade)
homens = [(nome[i], idade[i]) for i in range(len(nome)) if sexo[i].lower() == 'm']
mulher = [(nome[i], idade [i]) for i in range(len(nome)) if sexo[i].lower() == 'f' and idade[i] < 20]

velho = max(homens, key=lambda x: x[1])tg
nova = min(mulher, key=lambda x: x[1])
print (f'A média de idade do grupo é {media}. A pessoa mais velha é {velho[0]}. As mulheres tem menos de 20 anos são {len(mulher)}')


