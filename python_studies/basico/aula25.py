#Entendendo o FOR #

'''

Iteravél -> str, range, etc (__iter__)
Iterador -> quem vai entregar um valor por vez
next -> me entregue o próximo valor 
iter -> me entregue seu iterador

'''

"""
print (texto.__next__())
print (texto.__next__())
print (texto.__next__())
print (texto.__next__())
"""

'''
print (next(texto))
print (next(texto))
print (next(texto))
print (next(texto))

'''
# for letra in texto

texto = ('Luiz') # iterável
iterador = iter(texto) # iterador 

while True:
    try:
        letra = next(iterador)
        print (letra)
    except StopIteration:
        break

print (f"{'-' * 10}")

for letra in texto:
    print (letra)






