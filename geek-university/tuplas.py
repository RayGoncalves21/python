'''
tuplas (tuple)

tuplas são bastante parecidas com listas
são basicamente duas diferenças:
1- as tuplas são representadas por parenteses
    print(type(()))
2 - As tuplas são imutaveis, isso significa que ao se criar uma tupla ela não muda
toda operação em uma tupla, gera uma nova tupla    

Dicas na ultilização de tuplas: devemos ultilizar tuplas sempre que não precisarmos modificar os dados contidos em uma coleção
ex: meses


'''

tupla1 = (1,2,3,4,5,6)
print(tupla1)

tupla2 = 1,2,3,4,5,6
print(tupla2)
print(type(tupla2))

#não é uma tupla - é um int

tupla3 = (4)
print(tupla3)

print(type(tupla3))

tupla4 = (4,)
print(tupla4)
print(type(tupla4))

#conclusão, podemos concluir que tuplas são definidas pela virgula e não pelo uso do parenteses

#tupla com range
tupla5 = tuple(range(11))
print(tupla5)

tupla6 = ('Geek university', 'programação em python: essencial')

escola, curso = tupla6
print(escola)
print(curso)

# metodos para adição e remoção de elementos nas tuplas não existem

#soma, valor maximo, minimo e tamanho - apenas valores inteiros e reais

tupla7 = (4,5,6)

print(sum(tupla7))
print(max(tupla7))
print(min(tupla7))
print(len(tupla7))


#contatenação de tuplas 

print('contatenação das tuplas:', tupla1+tupla7)
print('tupla 1',tupla1)
print('tupla 7', tupla7)

#verificar de um elemento está contido na tuplas

print(4 in tupla7)

#iterando sobre uma tupla

for n in tupla1:
    print(n)

for indice, valor in enumerate(tupla1):
    print(indice, valor)  

#contado elementos dentro de uma tupla:

tupla8 = ('a','b','c', 'd', 'a', 'a')

print(tupla8.count('a'))


meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho','agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

print(meses[5])
print(meses)

# iterar com while

i =0
while i< len(meses):
    print(meses[i])
    i = i + 1


# slicing
# tupla(inicio:fim:passo)

print(meses[5:12:2])


