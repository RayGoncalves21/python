'''
deque - é uma lista de alta performance

'''

from collections import deque

# criando deques

deq = deque('Ray')
print(deq)

# adicionando elementos no deque

deq.append('y')
print(deq)

# adicionando no começo da lista

deq.appendleft('O')
print(deq)

# remover elementos

print(deq.pop()) # remove e retorna o ultimo elemento

print(deq.popleft()) # remove e retorna o ultimo elemento