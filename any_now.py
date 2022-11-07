'''
Any e all

all() -> retorna TRUE se todos os elemento do iterável são verdadeiros iou ainda se o iterável estiver vazio

any() -> Retorna True se qualquer do iterável for verdadeiro se o iterável estiver vazio retorna False


'''

# exemplo all

print(all([0, 1, 2, 3, 4, 5])) # todos os numeros sao verdadeiros? - False o zero é falso
print(all([1, 2, 3, 4, 5]))

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']
print(all([nome[0] == 'C' for nome in nomes]))

print(all([letra for letra in 'eio' if letra in 'aeiou']))
# obs: um iterável vazio convertido em boolean é false mas o all() entende como true

print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))



##### ANY ######

print(any([0, 1, 2, 3, 4])) # True

print(any([0, False, {}, (), []])) # False

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']

print(any([nome[0] == 'C' for nome in nomes]))




