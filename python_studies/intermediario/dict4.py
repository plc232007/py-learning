# Manipulando chaves e valores em dicionários

pessoa = {}

chave = 'nome'

pessoa[chave] = 'Elomar'
pessoa ['sobrenome'] = 'Miranda'

print (pessoa[chave])

pessoa[chave] = 'Maria'

# del pessoa['sobrenome']
print (pessoa)
print (pessoa['nome'])

print (pessoa.get('sobrenome', None))

if pessoa.get('sobrenome') :
  print ('Isso existe!!!!')

