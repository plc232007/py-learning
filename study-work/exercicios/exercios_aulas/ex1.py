'''
nome = 'Pedro'

print (f"Meu nome é {nome}")

'''
'''


nome = input ("Qual o seu nome? ")
idade = input ("Qual a sua idade? ")
idade_int = int(idade)

print (f"{nome} tem  {idade_int} anos.")

'''

'''
numero_1 = input ("Digite um numero: ")
numero_1_int = int (numero_1)

numero_2 = input ("Digite um numero: ")
numero_2_int = int (numero_2)

print (f"A soma entre {numero_1_int} e {numero_2_int} é {numero_1_int + numero_2_int} .")

'''

''' 

nome = input ("Qual o seu nome? ")
idade = input ("Qual a sua idade? ")
idade_int = int(idade)

print (f"Nome : {nome} \nIdade : {idade_int}")

'''

''' 
numb_1 = input("Informe um valor: ")
numb_int_1 = int (numb_1)
numb_2 = input("Informe um valor: ")
numb_int_2 = int (numb_2)

print (f"{numb_int_1} '+' {numb_int_2} = {numb_int_1 + numb_int_2}")
print (f"{numb_int_1} '-' {numb_int_2} = {numb_int_1 - numb_int_2}")
print (f"{numb_int_1} '*' {numb_int_2} = {numb_int_1 * numb_int_2}")
print (f"{numb_int_1} '/' {numb_int_2} = {numb_int_1 / numb_int_2:.4f}")

'''
'''

base = input("Infome a base: ")
base_int = int(base)
exp = input ("Informe o expoente: ")
exp_int = int(exp)

print (f"{base_int} elevado a {exp_int} é {base_int ** exp_int}")

'''
'''

n1 = input ("Nota 1: ")
n1_int = int (n1)
n2 = input ("Nota 2: ")
n2_int = int(n2)
n3 = input ("Nota 3: ")
n3_int = int (n3)


print (f"A média das notas é: {(n1_int + n2_int + n3_int) / 3}")

'''

numb = input ("Informe um valor: ")
int_numb = int (numb)

if int_numb % 2 == 0 :
    print (f"O numero {int_numb} é par {'!' * 3}")
else:
    print (f"O numero {int_numb} é impar {'!' * 3}")







































