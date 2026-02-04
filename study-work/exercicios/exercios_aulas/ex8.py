"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

"""
try:
    hora = float(input("Que horas são? "))

    if 0 <= hora < 12:
        saudacao = "Bom dia!"
    elif 12 <= hora < 18:
        saudacao = "Boa tarde!"
    elif 18 <= hora <= 23:
        saudacao = "Boa noite!"
    else:
        saudacao = "Horário inválido."

    print(f"{saudacao}")

except ValueError:
    print("Isso não é um número.")
