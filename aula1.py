a = 'Hello World'
print('Replace method: ' + a.replace('H', 'J'))

#  SPLIT METHOD
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#  STRING CONCATENATION 
a = 'Hello '
b = 'world'
c = a + b
print('String Contatenation: ' + c) 

#  FORMAT METHOD
# Não é possivel concatenar strings com inteiros, somente com o método format
quantidade = 10
price = 25.90
txt = 'Você comprou {} maçãs e custou {}'

print(txt.format(quantidade, price))    

#  LISTS
fruits = ['banana', 'kiwi', 'apple']
print(fruits)