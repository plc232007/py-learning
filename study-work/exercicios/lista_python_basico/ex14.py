"""
Exercício 14: Contar ocorrências
Conte quantas vezes a letra 'a' aparece na palavra 'paralelepípedo' usando for.
"""

nome = 'paralelepipedo'

conta = 0

for i in nome:
    if i == 'a':
        conta += 1

print(conta)