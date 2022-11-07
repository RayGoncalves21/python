'''
Teste de memoria com Generators

Ocupam menos memoria

416 MB de diferença entre a lista e os generators

# função usando listas 449 MB
def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums


# teste 449 mb de memoria

for n in fib_lista(100000):
    print(n)

'''



# FUnção usando geradores

def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador = contador + 1

# teste 2 com Geradores 2.8 MB

for n in fib_gen(100000):
    print(n)