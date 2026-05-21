'''
Crie um programa que:

Receba uma frase

Conte quantas vezes cada letra aparece

Ignore espaços

--- Não entendi muito bem o que é essa questão do dicionário! Farei depois.

'''

frase = input ('Informe uma frase: ')

i = 0

while i < len(frase):
    letra = frase = frase[i].lower

    if letra == '' : 
        i += 1
        continue 
    
    # TODO: atualizar  o dicionário aqui 
    