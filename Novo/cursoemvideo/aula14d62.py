#Melhore o DESAFIO 61, perguuntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

primeiro = int (input('Digite o primeiro termo '))
razao = int (input('Digite a razão '))
c = 1
termo = primeiro
cont = 1
total = 0
mais = 10
while mais !=0:
    total = total + mais
    while cont <= total:
        print(f'{termo} ->', end='')
        termo += razao
        cont += 1
    print ('Pausa')
    mais = int (input('Quantos termos você quer mostrar mais? '))
print (f'Progressão finalizada com {total} termos mostrados')
