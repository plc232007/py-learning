frase = "aaaaooo"

i = 0
maior_contagem = 0
letra_mais_frequente = ""

while i < len(frase):
    letra = frase[i]

    if letra == " ":
        i += 1
        continue

    contagem = frase.count(letra)

    if contagem > maior_contagem:
        maior_contagem = contagem
        letra_mais_frequente = letra

    i += 1

print(
    f"A letra que aparece mais vezes foi "
    f"'{letra_mais_frequente}', que apareceu "
    f"{maior_contagem}x"
)
