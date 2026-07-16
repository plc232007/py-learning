# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    # 'idade': 900,
}

#print (pessoa.__len__()) # quantidade de elementos no dicionario

#print (len(pessoa))

###print (chave, valor)

# print (pessoa.items())

pessoa.setdefault('idade', 9) # define um valor como padrao para sempre que essa chave for chamada
print(pessoa['idade'])



