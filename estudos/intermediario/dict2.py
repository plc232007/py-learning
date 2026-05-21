enge_funcionario = {
    
    'nome' : 'Pedro Leite Campos',
    'cargo' : 'Estagiário',
    'idade' : 18,
    'materias_faculdade' : [
        {'calculo', 'alegra', 'estutura de dados'}
    ],
    'contrato' : 'OK',
    
    
}

for chave in enge_funcionario:
    print(enge_funcionario[chave])
    
enge_funcionario['tempo'] = '1 ano'

print (f'{20*'-'}')
print (f'Lista Atualizada')
print (f'{20*'-'}')

for chave in enge_funcionario:
    print(chave, enge_funcionario[chave])