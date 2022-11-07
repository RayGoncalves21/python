'''
Ordered dict

é um dicionario que nos garante a ordem de inserção dos elementos

'''
from collections import OrderedDict


dicionario = {'a': 1, 'b': 2, 'c':3, 'd':4, 'e':5}

for chave, valor in dicionario.items():
    print(f'chave={chave}: valor {valor}')

# usando ordered

dicionario2 = OrderedDict({'a': 1, 'b': 2, 'c':3, 'd':4, 'e':5})

for chave, valor in dicionario2.items():
    print(f'chave={chave}: valor {valor}')


# Entendendo a diferença entre dict e ordered dict

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
print(dict1 == dict2) #true or false? - true - no dicionario a ordem não importa

# ordered dict

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1}) 
print(odict1 == odict2) # true or false? False - a ordem dos elementos importa para os orderes dict