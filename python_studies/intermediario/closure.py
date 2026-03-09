def criar_mult (multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_mult(2)
print (duplicar(2))

triplicar = criar_mult(3)
print (triplicar(3))

quadru = criar_mult(4)
print (quadru(4))