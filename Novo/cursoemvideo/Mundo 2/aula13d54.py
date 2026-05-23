#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantaas pessoas ainda não atingiram a maioridade e quantas já são maiores.
import datetime
ano = []
for idade in range(1, 8):
    nascimento = int (input(f'Digite o {idade} ano do seu aniversário '))
    dataexata = datetime.date.today().year
    conta = dataexata - nascimento
    ano.append(conta)
    adulto = [idade for idade in ano if idade >=18]
    jovem = [idade for idade in ano if idade < 18]
    
print(f'Ao todo tivemos {len(adulto)} pessoas maiores de idade \n e também tivemos {len(jovem)} pessoas menores de idade')



