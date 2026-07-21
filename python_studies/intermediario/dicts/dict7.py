p1 = {

  'nome' : 'Luiz',
  'sobrenome' : 'Miranda',

}

# print (p1.get('nome'))

# nome = p1.pop('nome')
# rint (nome)
# print (p1)

p1.update ({

  'nome' : 'Valor novo ',
  'idade' : 90,

})

print (p1)


# dá para fazer com argumentos nomeados

p1.update(nome = 'Epaminondas', idade=29)
print (p1)
