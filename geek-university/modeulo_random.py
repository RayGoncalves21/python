'''
Moddulo random e o que são modulos

em python, modulo nada mais são do que outros arquivos python

random -> possui várias funções para geração de números pseudoaleatorios
pode ser que haja repetição
# obs existem duas formas de se utilizar um modulo ou função deste


#forma 1 - importando todo o modelo (não recomendado)

import random

# ao realizar o import de todo o modulo todas as funções atributos, classes e propriedades que estiverem dentro do modulo, ficaram disponiveis em memoria
# caso saiba quais as funções usar utilize a forma 2

print(random.random())


# GERA UM NUMERO ALEATORIO ENTRE 0 E 1
# PARA USAR A FUNÇÃO RANDOM() DO PACOTE NOS COLOCAMOS O NOME DO PACOTE E O NOME DA FUNÇÃO SEPARADOS POR PONTO
# NÃO CONFUNDA A FUNÇÃO COM O PACOTE RANDOM - É UMA FUNÇÃO DO MODULO RANDOM


'''

# FORMA DOIS IMPORTANDO UMA FUNÇÃO ESPECIFICA DO MODULO
#forma recomendada poque podemos ussar direto
from random import random
from random import uniform
from random import randint
from random import choice
from random import shuffle


for i in range(10):
    print(random())

# uniform() -> gerar um numero pseudo aleatorio entre os valores estabelecidos - import uniform

for i in range(10):
    print(uniform(3, 7)) # 7 não é incluido


# randint() -> gera valores pseudoaleatorios entre os valores estabelecidos INTERIROS


# gerador aleatorio para mega sena

for i in range(6):
    print(randint(1,61), end=', ') # COMEÇA EM 1 E VAI ATÉ 60


# choice() -> mostra um valor aleatorio entre um iteravel

jogadas = ['pedra', 'papel', 'tesoura']

print(choice(jogadas))

# shuffle() -> tem a função de embaralhar dados

cartas = ['k', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10']

shuffle(cartas)
print(cartas)
print(cartas[0], cartas[1])