#empacotamento e desempacotamento de dicts
# relembrando conceitos

a, b = 1, 2 # inversão de valores
a, b = b, a

# print (a, b)

#(a1, a2), (b1, b2) = pessoa.items()

#print (a1, a2)
#print (b1, b2)

#for chave, valor in pessoa:
#    print (chave, valor)

pessoa = {

    'nome' : 'Aline',
    'sobrenome' : 'Souza'

}

dados_pessoa = {
    'idade' : 17,
    'altura' : 1.7,

}

pessoa_completa = {**pessoa, **dados_pessoa}

print (pessoa_completa)

def mostro_argumentos_nomeados(*args, **kwargs): # assim a função pode receber tanto argumentos nomeados quanto argumentos não nomeados
    print ('NÃO NOMEADOS', args)

    for chave, valor in kwargs.items():
        print (chave, valor)


#mostro_argumentos_nomeados(2391293, '232343432432oijfwdf', nome= 'joana', )
mostro_argumentos_nomeados (**pessoa_completa)

configuracoes = {

    'args1' : 1,
    'args2' : 2,
    'args3' : 3,
    'args4' : 4,
    'args5' : 5,
}

mostro_argumentos_nomeados(**configuracoes)
