numero_1 = input ('Informe um numero: ')
numero_1_int = int(numero_1)
numero_2 = input ('Informe outro numero: ')
numero_2_int = int (numero_2)
operador = input ('Informe o operador: ')

if operador == '+':
    print (numero_1_int, '+', numero_2_int, '=', numero_1_int + numero_2_int)

elif operador == '-' :
    print (numero_1_int, '-', numero_2_int, '=', numero_1_int - numero_2_int)

elif operador == '*' :
    print (numero_1_int, '*', numero_2_int,'=', numero_1_int * numero_2_int)

elif operador == '/' :
    print (numero_1_int, '/', numero_2_int,'=', numero_1_int / numero_2_int)

elif operador == '^' :
    print (numero_1_int, '^', numero_2_int, '=', numero_1_int ** numero_2_int)

else :
    print ('Operador errado!')