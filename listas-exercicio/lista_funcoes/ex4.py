# Utilizando a formula matemática!


""" 
def soma_ate(n):
   soma = (1+n) * (n/2)
 return soma

soma_ate_dez = soma_ate(10)

print (soma_ate_dez)

soma_ate_onze = soma_ate(11)

print (soma_ate_onze) 

"""
def soma_ate(n):

    soma = 0
    for i in range(1, n + 1):
        soma += i
        
    return soma

soma_ate_dez = soma_ate(10)

print (soma_ate_dez)

soma_ate_onze = soma_ate(11)

print (soma_ate_onze) 

