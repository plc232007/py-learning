"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.

"""


try:
    numero = int(input("Digite um número inteiro: "))
    
    if numero % 2 == 0: 
        print (f"O numero {numero} é par.")
    else:
        print (f"O numero {numero} é impar.")
except ValueError:
    print ("Isso não é um número inteiro.")