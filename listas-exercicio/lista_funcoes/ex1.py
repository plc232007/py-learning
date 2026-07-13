def saudacao(nome):

    return f'Ola, {nome} !'

gabi = saudacao('gabi')

print (gabi)

pedro = saudacao('Pedro')

print (pedro)

# O return faz com que a função entregue um valor concreto quando chamada, seja string, int ou o que seja, já o print não entrega um valor, só um texto. Isso pode causar problemas.
