'''
Dada uma lista de nomes:

nomes = ["Ana", "João", "Carlos", "Maria"]


Use while para procurar um nome digitado

Se encontrar, use break

Se não encontrar, o else do while deve exibir:

"Nome não encontrado"

'''

nomes = ["Ana", "João", "Carlos", "Maria"]
nome_usuario = input("Informe seu nome: ")

i = 0
while i < len(nomes):
    if nomes[i] == nome_usuario:
        print("Nome encontrado!")
        break
    i += 1
else:
    print("Nome não encontrado")