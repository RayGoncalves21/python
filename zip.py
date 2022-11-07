'''
zip() -> cria um iterável (zip object) que agrega elemento de cada um dos iteraveis como entrada em pares

SÓ PODE SER USADO UMA VEZ OS DADOS

o zip utiliza como parametro o menor tamanho em iteravel,
ou seja, se estiver trabalhando com iteraveis de tamanhos diferentes, vai
para quando os elementos da menor acabar
'''


lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2, 'abc')

print(zip1)
print(type(zip1))

print(tuple(zip1))

zip1 = zip(lista1, lista2, 'abcdef')
print(list(zip1))



prova1 = [80, 91, 78]
prova2 = [98, 89,53]
alunos = ['Maria', 'Pedro', 'Carla']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}

print(final)

# todas as notas
print(list(zip(alunos, prova1, prova2)))

# soma


