nome = 'Pedro'
preco = 381209389.11

variavel = "%s, o preço é R$%.2f" % (nome, preco) #Muito parecido com C!!
print (variavel)
print("O hexadecimal de %d é %08x" % (232, 232))

nome = "Pedro"
idade = 18
altura = 1.90

if True:
    print("Nome: %s\nIdade: %d\nAltura: %.2f" % (nome, idade, altura))
elif False:
    print("Nome: {}\nIdade: {}\nAltura: {}".format(nome, idade, altura))
    
else:
    print(f"Nome: {nome}\nIdade: {idade}\nAltura: {altura}")
    










