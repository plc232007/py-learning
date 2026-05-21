"""
Peça dois números

Tente dividir o primeiro pelo segundo

Trate:

divisão por zero

entrada inválida

"""
try: 
    
    numerador = float(input("Numerador :\n"))
    denominador = float(input("Denominador: \n"))
    divisao = numerador / denominador
    print (f'O valor da divisão entre {numerador} e {denominador} é {divisao:.2f}')

except:
    print('Algo deu errado.')
    