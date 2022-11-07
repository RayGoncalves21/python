'''
Named tuple -> São tuplas diferenciadas onde especificamos um nome para a mesm
e também parametros


'''

from collections import namedtuple
from traceback import print_tb

#precisamos definir o nome parametros

# forma 1 - declaração named tuple

cachorro = namedtuple('cachorro', 'idade raça nome')

# forma 2 - declaração da tuple
cachorro = namedtuple('cachorro', 'idade, raca, nome')

#forma 3 - declaração

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

#utilizando

ray = cachorro(idade=2, raca='chow-chow', nome= 'Ray')
print(ray)

print(ray[0]) # idade
print(ray[1]) # raça
print(ray[2]) # nome

# forma 2 

print(ray.idade)
print(ray.raca)
print(ray.nome)

