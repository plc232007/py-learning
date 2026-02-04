'''
Crie um loop que:

Percorra números de 1 a 20

Ignore números pares (continue)

Pare o loop ao chegar no número 15 (break)

Exiba apenas os números ímpares até esse ponto

'''

i = 0

while i <= 20:
    
    i += 1

    if i % 2 != 0:
        print (f'{'-' * 5 }    {i=}    {'-' * 5 }')
    elif i > 15:
        break
    else:
        continue
    if i + 1 < 16:
        
        print (f'Pulei o numero {i+1}')
        
else: 
    print ('Algo deu errado.')    
    
i = 1

while i <= 20:

    if i == 15:
        break

    if i % 2 == 0:
        i += 1
        continue

    print(i)
    i += 1
    