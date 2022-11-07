'''
Entendendo Iterators e Iterables

Iterator ->
    - Objeto que pode ser iterado
    - Objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada

Iterable ->
    - Objeto que retornará um iterator quando a funcao iter() for chamada
'''

nome = 'Geek' # é um iterable mas não é iterator
numeros = [1, 2, 3, 4, 5, 6] # é um iterable mas não é um iterator

it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))

print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))





