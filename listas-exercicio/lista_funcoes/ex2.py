def area_retangulo (base, altura):

    if base > 0 and altura > 0:

        return base * altura
    
    else:

        print ("Valores inválidos!")


def preco_piso (area, preco_m2):
    return area * preco_m2

base = float(input('Base: '))
altura = float(input('Altura: '))

area = area_retangulo (base, altura)
print ('Area: ', area)

preco_m2 = float(input('Preço por m²: '))

preco = preco_piso(area, preco_m2)

print ('Total : R$ ', preco)



