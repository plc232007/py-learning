
#Definição 

def soma (x, y, z): # Aqui estão os parametros
    print (f'{x=} {y=} {z=}', '|','x + y + z = ', x + y + z)


soma(1,2,3)
# soma (1, y=2, 5), após colocar um argumento posicional, você só pode adicionar argumentos posicionais

soma (y=3, x=3, z= -9)
