'''
Crie um sistema que:

Peça idade do usuário

Valide entrada com try/except

Use while para repetir até ser válido

Use if/else

Se idade for None ou inválida, trate corretamente

Exiba:

"Menor de idade"

"Maior de idade"

'''
while True:
    try:
        idade_str = input("Informe sua idade: ").strip()

        if idade_str == "":
            print("Idade não pode ser vazia")
            continue

        idade = int(idade_str)

        if idade < 0:
            print("Idade não pode ser negativa")
            continue

        # Se chegou aqui, a idade é válida
        break

    except ValueError:
        print("Digite um número inteiro válido")
