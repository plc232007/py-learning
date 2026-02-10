"""
Exercício 21: Encontrar máximo e mínimo
Dada a lista [34, 12, 89, 5, 67, 23, 91, 45], encontre o maior e o menor número usando
for (sem usar max() e min()).
"""
lista = [34, 12, 89, 5, 67, 23, 91, 45]

maior = lista[0] # Isso por que ele já começa checando um valor da própria lista!
menor = lista[0]

for i in lista:
    if i > maior:
        maior = i
    if i < menor:
        menor = i 

print (f'O maior valor da lista é: {maior}')
print(f'O menor valor da lista é: {menor}')