"""
Exercício 23: Remover duplicatas
Dada a lista [1, 2, 2, 3, 4, 4, 5, 1, 6], crie uma nova lista sem elementos repetidos
(mantendo a ordem).
"""

lista_com_erros = [1, 2, 2, 3, 4, 4, 5, 1, 6]
lista_sem_erros = []

for i in lista_com_erros:
    if i not in lista_sem_erros:
        lista_sem_erros.append(i)

print (lista_sem_erros)