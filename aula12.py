#estudo de fstring

nome = 'Pedro Leite Campos'
altura = 1.90
peso = 90
imc = peso / altura ** 2

print (nome, 'tem ', altura, 'de altura, pesa', peso, 'quilos e seu IMC é ', imc)

linha_1 = f'{nome} tem altura de {altura} pesa {peso:.2f} quilos e seu IMC é {imc:.2f}'

print (linha_1)