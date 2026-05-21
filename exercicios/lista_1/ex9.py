"""
Exercício 9: Ordenar lista
Dada a lista [45, 12, 89, 3, 67, 23], ordene-a em ordem crescente e decrescente.
"""

lista = [45, 12, 89, 3, 67, 23]

lista_crescente = sorted(lista, reverse=False)
lista_decrescente = sorted(lista, reverse=True)

print('Lista Crescente:', lista_crescente)
print('Lista Decrescente:', lista_decrescente)