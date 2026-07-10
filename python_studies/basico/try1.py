while True:
    try:
        entrada = input("Digite o ano em que você nasceu: ")
        ano = int(entrada)
        
        # Se a linha de cima falhar, o Python pula direto para o 'except'.
        # Se der certo, ele continua e executa o 'break', saindo do loop.
        
        print(f"Sucesso! O ano registrado foi {ano}.")
        break 

    except ValueError:
        # Informa o erro e, como o loop não foi quebrado, volta para o início do 'while'.
        print("Erro: Por favor, digite apenas números. Tente novamente.\n")