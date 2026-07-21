# Shalow copy vs Deep copy

d1 = {

  'c1' : 1,
  'c2' : 2,
  'l1' : [0,1,2],

}

# d2 = d1 # mesmo dicionário na memória, tudo o que você fizer com um vai acarretar no outro (deep copy)
d2 = d1.copy() # shalow copy

d2['c1'] = 1000

print (d1)


