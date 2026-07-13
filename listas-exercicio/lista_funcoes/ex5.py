def criar_usuario(nome, idade, cidade):
    texto = f'Dados: Nome : {nome} | Idade : {idade} | Cidade : {cidade}'
    return texto

user1 = criar_usuario('pedro', 19, 'bsb')
print (user1)

user2 = criar_usuario (idade = 70, nome = 'Elomar', cidade = 'goias')
print (user2)

user3 = criar_usuario('maria', 25, cidade = 'rj')
print (user3)

# erro = criar_usuario('maria', idade=70, 'rj')
# print(erro)


# Após um argumento posicional, só se pode colocar argumentos posicionais. 