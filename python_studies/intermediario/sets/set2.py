# Métodos úteis 
# add, update, clear, discard 

s1 = set()
s1.add('Luiz') # só aceita um valor por vez
s1.add(1)

s1.update(("ola mundo",1,2,2,3)) #iterado
# s1.clear()
s1.discard('ola mundo')

print (s1)
