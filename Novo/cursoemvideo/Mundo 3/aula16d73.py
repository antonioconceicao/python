#Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato BRASILEIRO DE FUTEBOL, na ordem da colocação. Depois mostre:
#a - Apenas os 5 primeiros colocados.
#b- Os últimos 4 colocados da tabela
#c- Uma lista com os times em ordem alfabética
#d - Em que posição na tabela está o time da Chapecoense.

campeonato = ('Flamengo', 'Palmeiras', 'Athletico-PR','Bahia','Fluminense', 'Cruzeiro', 'Atlético-MG', 'Coritiba','Bragantino', 'Santos', 'Botafogo', 'São Paulo', 'Vitória','Corinthians', 'Mirassol', 'Grêmio', 'Vasco','Internacional', 'Remo', 'Chapecoense')

print ('Campeonato Brasileiro 2026')

while True:
    print ('Escolha uma dessas opções\n a - Apenas os 5 primieros colocados \n b - Os últimos 4 colocados da tabela \n c - Uma lista com os times em ordem alfabética \n d - Em que posição na tabela está o time da Chapecoense \n e - Sair')


    escolher = input ('Digite uma letra para escolher a opção: ')
    minuscula = escolher.lower()
    print(f'Você digitou: {minuscula}')


    if minuscula == 'a':
        print (f'Os 5 primeiros colocados são:\n {campeonato[0:5]} ')

    if minuscula == 'b':
        print (f'Os últimos 4 colocados na tabela são:\n {campeonato[16:20]} ')

    if minuscula == 'c':
        lista = list(campeonato)
        lista.sort()
        print (f'Os times em ordem alfabética: \n {lista}')

    if minuscula == 'd':
        linha = campeonato.index("Chapecoense") + 1
        print (f'A chapecoense está na posição: {linha}')


    if minuscula == 'e':
        print ('Fechando o programa!')
        break


