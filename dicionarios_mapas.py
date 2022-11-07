'''
Em algumas linguagens de programação os dicionarios em py são conhecidos por mapas

são coleções do tipo chave/valor

Dicionarios são representados por chaves
    print(type({}))

sobre dicionarios
- Chave e valor são separados por dois pontos chave:valor
- Tanto chave quanto valor, podem ser de qualquer tipo de dados, podendo se misturar tipo de dados


'''
#forma 1 - mais comum
from traceback import print_tb


paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'paraguay'}
#         'chave': 'valor'

print(paises)
print(type(paises))

#forma 2 - menos comum

paises = dict(br = 'Brasil', eua = 'Estados unidos', py = 'paraguay')

print(paises)
print(type(paises))

#acessando elementos

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'paraguay'}

# forma 1 - acessando via chave da mesma forma que lista/tupla
print(paises['br'])
print(paises['eua'])

# forma 2 - acessando via get - recomendado

print(paises.get('br'))
print(paises.get('ru')) # dado None, pois não tem no dicionario

# encontrando chaves

pais = paises.get('br')

if pais:
    print(f'encontrei o pais {pais}')
else:
    print('não encontrei o pais')

print()
# ou de maneira simplificada

pais = paises.get('ru', 'não encontrado') # procura 'ru', se não encontrar mostra a mensagem depois da virgula
print()
print(f'encontrei o pais {pais}')


carrinho = []

produto1 = ['playstation 5', 1, 2300.00]
produto2 = ['good of war', 2, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)


# usando tuplas

produto3 = ('Ps5', 1, 2500.00)
produto4 = ('God of war 4', 5, 250.00)
carrinho = (produto3, produto4)

print(carrinho)


#dicionario 

carrinho = []


produto1 = {'nome: ': 'playstatio5', 'qt': 1, 'preco': 2300.00}
produto2 = {'nome': 'good of war', 'qt': 5, 'preco': 125} 

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)


d = dict(a =1, b = 2, c = 3)

print(d)
print(type(d))

# limpar o dicionarios - zerar dados

d.clear()
print(d)

#copiando um dicionario para outro

novo = d.copy()

print(novo)

novo['d'] = 4

print(d)
print(novo)



