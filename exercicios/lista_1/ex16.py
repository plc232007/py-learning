"""
Exercício 16: Enumerar elementos
Imprima cada elemento da lista ['Python', 'Java', 'C++', 'JavaScript'] junto com sua
posição (começando de 1).
"""

lista_linguagens = ['Python', 'Java', 'C++', 'JavaScript']
contagem = 1
for i in lista_linguagens:
    print(f'({contagem}, {lista_linguagens})')
    contagem += 1