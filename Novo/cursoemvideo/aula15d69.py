#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final mostre:                                      
#a - quantas pessoas tem mais de 18 anos.anos. 
#b - Quantos homens foram cadastrados.
#c -Quantas mulheres tem menos de 20 anos.

homens = 0
mulheres = 0
dezoitoanos = 0
mulhercom20 = 0


#soma = idade / 

print ('Cadastre uma pessoa')

while True:
    idade = int (input('Idade: '))
    sexo = input('Sexo: [M/F]')
    minuscula = sexo.lower()

    continuar = input ('Quer Continuar? [S/N]')
    minuscula2 = continuar.lower()

    if idade > 18:
        dezoitoanos += 1
    if (idade < 20) and (minuscula == 'f'):
        mulhercom20 += 1
    if minuscula == 'm':
        homens += 1


    
    else:
        print('-------fim do programa-----')
        print(f'Total de pessoas com mais de 18 anos: {dezoitoanos}')
        print (f'Ao todo temos {homens} homens cadastrados')
        print (f'E temos {mulhercom20} mulheres com menos de 20 anos')
        break