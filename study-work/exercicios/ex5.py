nome_aluno = input ("Qual o seu nome: ")
nota1 = input ("Informe a nota do primeiro bimestre: ")
nota1_int = int(nota1)
nota2 = input ("Informe a nota do segundo bimestre: ")
nota2_int = int(nota2)
nota3 = input ("Informe a nota do terceiro bimestre: ")
nota3_int = int(nota3)
nota4 = input ("Informe a nota do quarto bimestre: ")
nota4_int = int(nota4)

media = (nota1_int + nota2_int + nota3_int + nota4_int) / 4 

if media >= 7 : 
    print (f'Sua média foi : {media:.2f}, você passou')

elif 5 <= media < 7 : 
    print (f'Sua média foi : {media:.2f}, você está de recuperação, bocó')

else : 
    print (f'Sua média foi {media:.2f}, você é uma anta, não passou de ano :/ ')
