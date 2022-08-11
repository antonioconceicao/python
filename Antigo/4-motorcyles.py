motorcycles = ['honda','yamaha','suzuki']
print (motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)
#exemplo 3
motorcycles.insert(0, 'ducai')
print(motorcycles)

#4
del motorcycles[0]
print(motorcycles)
#pop() method
popped_motorcyle = motorcycles.pop()
print (motorcycles)
print (motorcycles)