"""
Exercício 17: Filtrar com for
Dada a lista [12, 7, 21, 4, 9, 18, 3, 15], crie uma nova lista apenas com números
maiores que 10.
"""

lista = [12, 7, 21, 4, 9, 18, 3, 15]
lista_maior_10 = []

for i in lista:
    if i > 10:
        lista_maior_10.append(i)

print (lista_maior_10)