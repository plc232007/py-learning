"""
Exercício 8: Concatenar listas
Crie duas listas: uma com números pares de 0 a 8 e outra com ímpares de 1 a 9. Concatene-as e
imprima o resultado
"""
lista_par = [0, 2, 4, 6, 8]
lista_impar = [1, 3, 5, 7, 9]

print ('Lista concatenada: ', lista_par + lista_impar, end = '\n')
lista_par.extend(lista_impar)
print (lista_par)