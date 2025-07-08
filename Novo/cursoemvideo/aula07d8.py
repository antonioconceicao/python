n1 = float (input('Digite o valor do metro '))
m = 1
c = 100
d = 1000 

# Referência das unidades (não utilizadas diretamente)

# km = 1000
# hm = 100
# dam = 10
# dm = 0.1

n2 = m / c
n3 = n1 / n2
n4 = n1 * d
n5 = n1 / 1000
n6 = n1 / 100
n7 = n1 / 10
n8 =  n1 * 10
print ('O centrímetro é {} \n o milimetro é {} \n o km é {} \n o hm é {} \n dam é {} \n o dm é {} ' .format(n3,n4, n5,n6, n7, n8 ))