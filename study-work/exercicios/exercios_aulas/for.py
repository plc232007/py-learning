senha_salva = '123456'
senha_digitada = input ('Informe a senha: ')
repeticoes = 0

while senha_salva != senha_digitada:
    senha_digitada = input(f'Sua senha ({repeticoes}x): \n')

    repeticoes += 1

print ('Senha correta!')