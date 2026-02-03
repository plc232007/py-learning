'''
Crie:

Uma variável com uma string

Uma variável com uma lista

Copie cada uma para outra variável

Altere a cópia

Observe o que acontece com a original


'''

texto_original = 'Olá'
texto_copia = texto_original

texto_copia = texto_copia + " mundo"

print (f'texto_original: {texto_original}')
print (f'texto_copia: {texto_copia}')

lista_original = [1, 2, 3]
lista_copia = lista_original

lista_copia.append(4)

print("lista_original:", lista_original)
print("lista_copia:", lista_copia)
