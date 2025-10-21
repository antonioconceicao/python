#Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro = int (input('Digite o primeiro termo '))
razao = int (input('Digite a razão '))
c = 1
guardardados = []

while c <= 10:
    pa = primeiro + (c -1) * razao
    c += 1
    guardardados.append(pa)

print ('Resultado',*guardardados)
