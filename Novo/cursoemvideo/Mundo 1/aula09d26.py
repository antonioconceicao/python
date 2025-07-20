# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra 'A'.
#Em que posição ela aparece a primeira vez.
#Em ve que posição ela aparece a ultima vcez.

text = input ('Digite uma frase pequena ').strip()
tratamento = text.lower()
letra = tratamento.count('a')
find = tratamento.find('a')
ultimo = tratamento.rfind('a')

print(f'O A nesse frase contem {letra} e ele aparece no {find} e a ultima vez é {ultimo}')
