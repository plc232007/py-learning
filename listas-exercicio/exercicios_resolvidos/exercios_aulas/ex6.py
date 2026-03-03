"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
    
"""

nome = input("Informe seu nome: ")
idade = input("Informe sua idade: ")

if nome and idade:
    print(f"{'Seu nome é':<30}{nome}")
    print(f"{'Seu nome invertido é':<30}{nome[::-1]}")

    if " " in nome:
        print(f"{'Seu nome contém espaços':<30}{'Sim'}")
    else:
        print(f"{'Seu nome contém espaços':<30}{'Não'}")

    print(f"{'Seu nome tem letras':<30}{len(nome)}")
    print(f"{'A primeira letra do nome é':<30}{nome[0]}")
    print(f"{'A última letra do nome é':<30}{nome[-1]}")

else:
    print("Desculpe, você deixou campos vazios.")
