#Refaça o DESAFIO 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#Equilátero: todos os lados iguais
#Isósceles: dois lados iguais
#Escaleno: todos os lados diferentes

primeiro = float(input ('Digite o primeiro segmento '))
segundo = float (input ('Digite o segundo segmento '))
terceiro = float (input('Digite o terceiro segmento '))

conta = abs(segundo - terceiro) < primeiro < segundo + terceiro
conta2 = abs(primeiro - terceiro )< segundo < primeiro + terceiro
conta3 = abs(primeiro - segundo) < terceiro < primeiro + segundo 


if conta and conta2 and conta3:
    print ('Esse valor consegue transformar em um triângulo')
    if primeiro == segundo == terceiro:
        print ('Ele é equilátero')
    elif  primeiro == segundo or primeiro == terceiro or segundo == terceiro:
        print ('Ele é Isósceles')
    else:
        print ('Todos os lados são diferentes')
else:
    print ('Esses valores não podem formar um triângulo')
