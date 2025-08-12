#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
#ex: Apos a sopa
#A sacada da casa
#A torre da derrota
#O lobo ama o bolo
#Anotaram a data da maratona

frase = input ('Digite uma frase ')
cortar = "".join(frase.split())
diminuir = cortar.lower()
palindromo = diminuir[::-1]

if palindromo == diminuir:
    print(f'a frase "{frase}" invertido fica {palindromo}. \n Essa frase é um Palíndromo')
else:
    print (f'a frase "{frase}" invertido fica {palindromo}. \n Essa frase NÃO é um Palíndromo')

