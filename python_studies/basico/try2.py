config = {"host": "localhost", "porta": 8080}

while True: 

    try:
        # O ponto crítico: tentar acessar uma chave que não foi definida
        senha_do_banco = config["senha"]
        print(f"A senha á {senha_do_banco}")

    except KeyError:
        # Captura a falha e exibe a mensagem amigável
        print ("A chave solicitada não foi encontrada nas configurações.")