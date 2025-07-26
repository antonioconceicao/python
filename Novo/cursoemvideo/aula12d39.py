# Faça um programa que leia o ano de nascimento de um jovem e conforme, de acordo com a sua idade:
#Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de se alistar.
#Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
dia = int (input('Digite o dia do seu nascimento '))
mes = int (input('Digite o mês do seu aniversario '))
ano = int (input('Digite o ano do nascimento '))
nascimento = date(ano, mes, dia)
dataatual = date.today()
dataano = date.today().year
idade = dataatual.year - nascimento.year
alistar = 18 - idade
print (alistar)

if alistar == 0:
    print ('Você tem 18 anos e precisa se alistar no exercito!')
elif alistar < 0:
    print ('Você já passou da data permitida para se alistar e entre em contato mais próximo do CEB')
else:
    print (f'Você ainda não tem idade para se alistar e falta {alistar} anos')


