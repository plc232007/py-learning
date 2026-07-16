#closures e funções que retornam outras funções

def criar_saudacao(saudacao, nome):

  def saudar ():

    return f'{saudacao}, {nome}'

  return saudar

s1 = criar_saudacao ('Bom dia', 'Pedro')

s2 = criar_saudacao ('Boa noite', 'Joao')

print (s1())
print (s2())



