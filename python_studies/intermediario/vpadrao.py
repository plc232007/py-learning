# Colocar um valor na função que pode ou não ser enviado. 

def soma (x, y, z = None) :
    if z is not None : 
        print (f'{x=} {y=} {z=}', x + y + z)
    else: 
        print (f'{x=} {y=}', x + y)

soma (1,2,3)
soma (1,3)