# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicador (*args):

    total = 1
    for i in args:
        total *= i

    return total   

mult1234 = multiplicador(1,2,3,4)
print (mult1234)


