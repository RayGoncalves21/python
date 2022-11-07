'''
Conjuntos - referencia a teoria dos conjuntos da matematica

os conjuntos são chamados de sets, da mesma forma que na matematica sets não possuem valores duplicados
sets não possuem valores ordenadores
Elementos não são acessados via indice - não são indexados

Conjuntos são bons para se utilizar quando precisamos armazenar elementos
mas não nos importamos da ordenação deles, sem procupáção com chaves, valores e items duplicados

Os conjuntos são referenciados em pyhon com chaves {}

Diferença entre conjuntos e mapas - 
     um dicionario tem chave/valor
     um conjunto tem apenas valor
'''

#Definindo um conjunto

#forma 1 
s = set({1,2,3,4,5,6,7,2,3}) #temos valores repetidos
print(s) # não adiciona valores repetidos
print(type(s))

# forma 2 - mais comum 

s = {1,2,3,4,5,6,7}
print(s)

#verificando se um elemento está contido no conjunto
if 3 in s:
    print('tem o numero 3')
else:
    print('não tem o 3')

# importante lembrar que além de não termos valores duplicados não temos ordem
dados = '99,2,32,23,1,44,5,2,32,34'

lista = list(dados)
print(f'listas: {lista}')

tupla = tuple(dados)
print(f'tuplas: {tupla}')

dicionario = {}.fromkeys(dados, 'dict')
print(f'dicionario: {dicionario}')

conjunto = set(dados)
print(f'Conjunto: {conjunto}')

#usos interessantes com sets

cidades = ['Belo Horizonte', 'São paulo', 'campo grande', 'cuiaba', 'campo grande', 'cuiaba']
print(cidades)
print(len(cidades))

#Agora precisar saber quantas cidades unicas temos
# podemos utilizar o set para isso

print(len(set(cidades)))

# adicionando elementos em um conjunto
s = {1,2,3}
s.add(4)
print(s)

#Remover elementos em um conjunto - não é indice, informamos o valor a ser removido

s.remove(2) # gera erro se não tiver o valor
print(s)

# modo2
s.discard(1) # não gera erro
print(s)

# deep copy - separados

novo = s.copy()
print(novo)

novo.add(4)
print(novo)
print(s)

# shallow copy 

novo = s
novo.add(5)
print(novo)
print(s)


# podemos remover todos os itens de um conjunto

s.clear()
print(s)

# metodos matematicos de conjuntos

# imagine que temos dois conjunto -
# 1 com estudantes de python
# segundo com estudante de java

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando',  'Gustavo', 'Julia', 'Ana', 'Patricia'}

# veja que alguns alunos estão nos dois cursos

# forma 1 - utilizando union

unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

# forma dois utilizzando pip |

unicos2 = estudantes_java | estudantes_python

print(unicos2)

# gerar um conjunto de estudantes que estão em ambos os cursos

# forma um utilizando o intercection

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)


# forma 2 utilizando o & comercial

ambos2 = estudantes_python & estudantes_java
print(ambos2)

# gerar um conjunto de estudantes apenas em um curso

so_pyhton = estudantes_python.difference(estudantes_java)
print(so_pyhton)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)