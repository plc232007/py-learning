'''
Receba o valor total de uma compra

Receba o número de parcelas

Use for + range

Mostre o valor de cada parcela numerada

Exemplo:

Parcela 1: R$ 100.00
Parcela 2: R$ 100.00

'''

valor = float(input('Qual foi o valor da compra: \n'))

parcelas = int(input('Foi dividido em quantas vezes: \n'))

mensal = valor / parcelas

parametro = range(0, parcelas, 1) 
'''
Isso nao precisa ser criado, pode ser feito da seguinte forma: 

for i in range(parcelas) : 
    print...
    
'''


i = 0 

for i in parametro:
    print (f'Mês {i+1} = {mensal:.2f}')