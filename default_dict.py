'''
Modulo Collections - Default Dict

Default dict - nos informamos o valor default
podendo utilizar em lambda para isso. esse valor será utilziado sempre que não houver um valor definido

'''

from collections import defaultdict


dicionario = {'curso': 'Programação em python: essencial'}
print(dicionario)
print(dicionario['curso'])

dicionario2 = defaultdict(lambda:0)

print(dicionario2)

dicionario['curso'] = 'programaçã em python: essencial'
print(dicionario2)