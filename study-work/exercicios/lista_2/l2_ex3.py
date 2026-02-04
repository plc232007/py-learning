'''
Crie um script que:

Atribua o mesmo valor a duas variáveis

Mostre o id() de cada uma

Depois altere uma delas e mostre novamente os id()
'''
numb_1 = 2

var_1 = numb_1
var_2 = numb_1 

print (id(var_1)) # Nesse caso da para ver que o pyhon reapreoveita na memória variavéis de valores iguai.
print ()
print (id(var_2))

numb_2 = 3

var_2 = numb_2

print ()
print (id(var_2))
