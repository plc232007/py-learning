numb1 = input ("Informe um valor: ")
numb1_int = int(numb1)

numb2 = input ("Informe outro valor: ")
numb2_int = int(numb2)

if numb1_int > numb2_int:
    print (f"{numb1_int} é maior que {numb2_int}")

elif numb2_int > numb1_int:
    print (f"{numb2_int} é maior que {numb1_int}")

else:
    print (f"{numb1_int} é igual a {numb2_int}")