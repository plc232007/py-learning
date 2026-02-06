lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
lista_d = lista_a.extend(lista_b) # extende a lista a para a lista b

print (lista_c)
print (lista_d) ## Utilizou um método que não retorna nada "None", o valor passou para a lista a

print (lista_a) # O valor veio para cá