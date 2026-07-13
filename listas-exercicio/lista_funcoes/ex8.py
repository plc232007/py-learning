def conecta(host, porta=8080):
    if porta == 8080:
        return f'{host}'
    else:
        return f'{host}.{porta}'
    
print (conecta('teste', 3000))
print (conecta('teste'))