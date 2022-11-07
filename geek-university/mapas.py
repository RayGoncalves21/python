# mapas - são representados por chaves {}

from calendar import c, prcal
import re


receita = {'jan': 100, 'fev': 250, 'mar': 350}

# interar sobre dicionarios

for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'{chave} : {receita[chave]}')

for chave in receita: 
    print(f'Em {chave} recebi R$: {receita[chave]}')

print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

# acessando os valores

for valor in receita.values():
    print(valor)

    # desenpacotamento de dicionarios

for chave, valor in receita.items():
    print(f'chave = {chave} e valor = {valor}')


# Soma, valor maximo, valor minimo e tamanho

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita.values()))