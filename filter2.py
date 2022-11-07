'''

paises = ['', 'Argentina', '', 'Brasil', 'Chile', 'Peru', 'Equador', '', 'Venezuela']

print(paises)

res = filter(None, paises)
# faz os dados varios serem eliminados
print(list(res))
# COm lambda
res2 = filter(lambda pais: len(pais) >0, paises)
print(list(res2))
# jeito 3
res3 = filter(lambda pais: pais != '', paises)
print(list(res3))

# diferença entre map() e filter()

map() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto maepando a função para cada elemento do iterável
filter() -> Recebe dois parâmetros, uma função e um iterável, e retorna um objeto filtrando apenas os elementos de acordo com a função
'''

# Exemplo mais complexo

usuarios = [
    {'username': 'Samuel', 'Tweets': ['Eu adoro bolos', 'eu adoro pizzas']},
    {'username': 'Carla', 'Tweets': ['Eu amo meu gato']},
    {'username': 'Jeff', 'Tweets': []},
    {'username': 'Bob123', 'Tweets': ['Eu gosto de cachorros', 'Vou sair hoje']},
    {'username': 'DeuJogo', 'Tweets': ['Cash na COnta', 'Saque rápido', 'maiores cotações']},
    {'username': 'Lucas', 'Tweets': []}
            ]
print(usuarios)
# Filtrar os usuarios que estão inativos no twitter

inativos = list(filter(lambda u: len(u['Tweets']) ==0, usuarios))

print(inativos)