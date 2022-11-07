'''

a difreneça entre o list comprehensions e generators é o () no generator e [] no lista c
só usa os dados uma unica vez
'''
from sys import getsizeof
nomes = ['Carlos', 'Camila', 'Cassiano', 'Cristina', 'Vanessa']
print(any(nome[0] =='C' for nome in nomes))

# list comprehensioons

res = [nome[0] == 'c' for nome in nomes]
print(type(res))
print(res)

# generator
res = (nome[0] == 'c' for nome in nomes)
print(type(res))
print(res)


# get size off
# retorna a quantidade de bytes em mémoria do elemento passado como parametro
print(getsizeof('Geek'))


## gerando uma lista de numeros com list comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

## gerando uma lista de numeros com set comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

## gerando uma lista de numeros com Dictonary comprehension
dic_comp = getsizeof({x * 10 for x in range(1000)})

## gerando uma lista de numeros com generators

gen = getsizeof(x * 10 for x in range(1000))

print('para fazer mesma tarefa gastamos em memória: ')
print(f'Lista Comp: {list_comp} bytes')
print(f'Set Comp: {set_comp} bytes')
print(f'dict Comp: {dic_comp} bytes')
print(f'generator: {gen} bytes')


# podemos iterar

gen = (x* 10 for x in range(1000))
for num in gen:
    print(num)