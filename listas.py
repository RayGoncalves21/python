

from distutils import core
import enum


carrinho = []
produto = ''


while produto != 'sair':
    print('Adicione um produto ao carrinho ou digite sair para sair')
    produto = input()

    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(produto)

    # ultilizando variaveis

print('-----------')

numeros = [2, 3, 4, 5]

cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0]) # verde
print(cores[1]) # amarelo
print(cores[2]) # azul
print(cores[3]) # branco

# forma indexada inversa 

print(cores[-1]) # branco
print(cores[-2]) # azul
print(cores[-3]) # amarelo
print(cores[-4]) # verde
#print(cores[-5]) # erro - pois não existe indice -5 


cores = ['verde', 'amarelo', 'azul', 'branco']

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores): # len =tamanho
    print(cores[indice])
    indice = indice + 1


# gerar indice em um for - saber a posição

for indice, cor in enumerate(cores):
    print(indice, cor)

# lsitas aceitam valores repetidos

lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)

print(lista)


# econtrar o indice de um elemento na lista

numeros = [5,6,7,5,8,9,10]
print(numeros.index(6))

#value erro - o item não existe na lista
#obs: retorna o primeiro indice em valores iguais

#podemos fazer busca dentro de um range

print(numeros.index(5, 1)) #buscando a partir do indice 1 - primeiro valor e depos o indice

#soma valor se fore interiros ou reais

lista = [1,2,3,4,5,6]

print(sum(lista))   # soma
print(max(lista))   # maximo valor
print(min(lista))   # minimo valor
print(len(lista))   # tamanho da lista

# Copiando uma lista para outra - shallow copy e deep copy

lista = [1,2,3]
print(lista)

nova = lista.copy()
print(nova)

nova.append(4)
print(nova)
# deep copy - copia mas são listas idenpendentes

lista = [1,2,3]
print(lista)

nova = lista #copia shallow
print(nova)

nova.append(4)
print(lista)
print(nova)
#ambas as listas foram alteradas