'''
Crie um programa que:

Use while dentro de while

Gere a tabuada de 1 até 5

Exemplo de saída esperada:

1 x 1 = 1
1 x 2 = 2
...

'''

antes = 1 # Antes do x 
depois = 1 # Depois do x

while antes <= 5:
    depois = 1
    
    while depois <= 5:
        print (f'{antes} x {depois} = {antes * depois}')
        depois += 1
    
    print (f'{'-' * 15}')
    antes += 1

print ('Acabou!')
    