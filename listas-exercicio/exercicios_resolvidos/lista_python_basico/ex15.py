"""
Exercício 15: Criar lista com for
Crie uma lista com os quadrados dos números de 1 a 10 usando for e append()
"""

lista_quadrados = []

valor = range(1, 11)

for i in valor: ##assim fica mais bonito
    lista_quadrados.append(i*i)

print (lista_quadrados)

