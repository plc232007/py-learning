#Calculador em python#

validacao = input("Calculadora ---- [S]im [N]ão \n")


while validacao == 'S':  

    numb_1 = input ("Informe o primeiro numero: ")
    float_numb_1 = float(numb_1)
    operador = input ("Informr o operador: ")
    numb_2 = input ("Informe o segundo numero: ")
    float_numb_2 = float(numb_2)

    if operador == '+':
        print(f'{float_numb_1} + {float_numb_2} = {float_numb_1 + float_numb_2}')
    elif operador == '-':
        print (f'{float_numb_1} - {float_numb_2} = {float_numb_1 - float_numb_2}')
    elif operador == '*':
        print (f'{float_numb_1} * {float_numb_2} = {float_numb_1 * float_numb_2}')
    elif operador == '/':
        if float_numb_2 == 0:
            print ("O divisor não pode ser zero!")
            continue
        else:
            print(f'{float_numb_1} / {float_numb_2} = {float_numb_1 / float_numb_2}')
    elif operador == '**':
        print (f'{float_numb_1} ** {float_numb_2} = {float_numb_1 ** float_numb_2}')

    validacao = input("Deseja continuar? [S]im [N]ão  \n")
    
    



