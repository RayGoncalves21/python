'''
NÂO CONFUNDA COM sort() que só pode ser usado em listas

podemos utilizar o sorted() com qualquer iterável

SORTED serve para ordenar elementos

não modifica a lista, ele gera uma nova
obs: o sorted, sempre retorna uma lista com os elementos do iterável ordenados

'''


# sort
numeros = [6, 1, 8, 2]

print(numeros)

print(sorted(numeros)) # ordenar

print(numeros)


print(sorted(numeros, reverse=True)) # ordena do maior para o menor


usuarios = [
    {"username": 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {"username": 'carla', 'tweets': ['Eu amo meu gato']},
    {"username": 'jeff', 'tweets': []},
    {"username": 'bob123', 'tweets': ['Rastaman']},
    {"username": 'doggo', 'tweets': ['Eu gosto de cachorros', 'vou sair hoje']},
    {"username": 'gal', 'tweets': [], 'cor': 'preto', 'musica': 'rock'}
]

print(usuarios)
# ordem alfabetica
print(sorted(usuarios, key=lambda usuario: usuario['username']))

# ordem numero de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario['tweets'])))


musicas = [
    {'titulo': 'Thunderstruck', 'tocou': 3},
    {'titulo': 'Dead skin Mask', 'tocou': 2},
    {'titulo': 'back in black', 'tocou': 4},
    {'titulo': 'Possik - ', 'tocou': 32},
]

# ordena a menos tocada para as mais tocadas
print(sorted(musicas, key = lambda musica: musica['tocou']))

# mais tocadas
print(sorted(musicas, key = lambda musica: musica['tocou'], reverse=True))



