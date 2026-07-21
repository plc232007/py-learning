## Funções lambda complexas não são boas práticas, isso pode dificultar desnecessáriamnente o código


def executa (funcao, *args) :
    return funcao(*args)

def soma (x, y) :
    return x + y

def criar_multiplicador(multiplicador) :
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

duplica = executa (

    lambda m:lambda n: n * m,
    2
)

print (

    executa(
        lambda x, y: x + y,
        2, 3
    ),
    executa(soma, 2, 3),
    soma(2, 3)

)

print (duplica(2))

