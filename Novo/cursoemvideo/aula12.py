nome = str (input('Qual é seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print ('Seu nome é bem popular no Brasil')
elif nome in 'Ana cLÁUDIA jÉSSICA jULIANA':
    print ('Belo nome feminino')
else:
    print ('Belo nome feminino')
print ('Tenha um bom dia, {}!' .format(nome))
