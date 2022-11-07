'''
O que java chama de arrays
- unidimensionais
- multidimencionais
'''

#exemplo
listas = ([1,2,3], [4,5,6], [7,8,9]) # matrix 3 x 3

print(list)
print(type(listas))

# como acessar os dados

print(listas[0][1])
# primeiro linha[0] coluna[1]

numero1 = listas[0][2]
numero2 = listas[2][2]

soma = numero1 + numero2

print(soma)


 # iterando com loops

for lista in listas:
    for num in listas:
        print(num)
# list comprehensions

[[print(valor) for valor in lista] for lista in listas]
