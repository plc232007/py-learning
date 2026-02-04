'''
Crie um sistema que:

1) Peça senha ao usuário 

2) Permita no máximo 3 tentativas

3) Use while '< 3'

Use break quando a senha estiver correta

'''

senha_salva = '123456'

i = 0; 

while (i < 3):
    
    senha_digitada = input ('Informe sua senha: \n')
    
    if senha_salva == senha_digitada:
        print ("Senha correta!") 
        break 
    else: 
        print ('Senha incorreta!')
    
    i += 1
else: 
    print ("Acesso bloqueado, quantidade de tentativas excedidas!")
    

    
