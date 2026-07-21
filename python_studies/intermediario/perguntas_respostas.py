perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]


total = 0

for pergunta in perguntas:

    print ('Pergunta: ', pergunta['Pergunta'])
    print()

    for i, opcao in enumerate (pergunta['Opções']):
        print (f'{i+1})', opcao)

    print ()


    resp = int(input('Qual é a resposta correta? '))
    print()

    valor = int(pergunta['Resposta'])

    if (resp == valor):

        total = total + 1
        print ("Resposta correta!")

    else:

        print ("Resposta Incorreta!")

    print ()


print (f'TOTAL DE ACERTOS : {total}')
