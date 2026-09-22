#Crie um programa que tenha uma tupla totalmente preenchida ccom uma contagem por extenso, de zero até vinte.
#Seu programa deverá ter um número pelo teclado (entre 0 a 20) e mostrá-lo por extenso.

nomeextenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze','dezesseis' , 'dezessete', 'dezoito', 'dezenove', 'vinte')


while True:
    usuario = int (input('Digite um número entre 0 e 20: '))

    if usuario > 20 or usuario < 0:
        print('Tente novamente.')
        continue
    

    escolhido = nomeextenso[usuario]
    break
print (f'Você escolheu o número: {escolhido}')




