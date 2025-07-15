# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas minúsculas.
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome.

n1 = input ('Digite o seu nome completo ').strip()

grande = n1.upper()
pequeno = n1.lower()
eliminar = len(n1.replace(" ", ""))
primeiro = len(n1.split()[0])

print (grande)
print (pequeno)
print (eliminar)
print(primeiro)
