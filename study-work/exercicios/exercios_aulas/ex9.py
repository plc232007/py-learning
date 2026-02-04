"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 

"""

nome = input ("Informe seu nome: ")

if len(nome) < 5 :
    resposta = "Seu nome é curto!"
elif 5 <= len(nome) <= 6:
    resposta = "Seu nome é normal."
else:
    resposta = "Seu nome é muito grande!"

print (f"{resposta}")