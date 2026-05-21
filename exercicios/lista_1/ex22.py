"""
Exercício 22: Lista de listas (matriz)
Crie uma matriz 3x3 (lista de listas) e use loops for aninhados para imprimir todos os elementos.
"""

matriz_ordem_tres = [[1,2,3], [4,5,6], [7,8,9]]

for linhas in matriz_ordem_tres:
    for elementos in linhas:
        print (elementos, end=' ')

    print ()