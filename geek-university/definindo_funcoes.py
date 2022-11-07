'''
Definindo funções
criar pequenas partes do codigo que executam tarefas expecificas
- pode não receber entradas de dados e retornar uma saidade e dados
- são uteis para executar procedimento similares por repetidas vezes
- fazer o mais simplificado possivel
'''

# exemplo de utilização

cores = ['verde','azul','amrelo', 'branco']

# utilizando a função integrada ( built-in ) do python

print(cores)

cores.append('roxo')
print(cores)


# Como definir funções
'''
a forma geral de definir uma função
é def nome_da_função(parametros_De_entrada):
    bloco da função

onde: nome da função smpre com letras minusculos e se for nomecomposto, separado por underline
- parametros de entrada são opcionais
- se for mais de um, separado por virgulas
'''

# Definindo a primeira função

def diz_oi():
    print('oi')

'''
obs: 1- dentro das nossas funções, podemos utilizar outras funções
    2- nossa função só executa uma tarefa, a unica coisa que ela faz é dizer oi
    3- essa função não recebe nenhum parametro de entrada.
    4- essa função não retorna nada

''' 
# utilizando funções
#chamada de execução
diz_oi()

# ATENÇÃO: nunca esqueça de utilizar o parenteses ao executar uma função

# ex 2

def cantar_parabens():
    print('parabéns pra você')
    print('nessa data querida')
    print('muitas felicidades')
    print('muitos anos de vida')
    print('---------------')

cantar_parabens()

for n in range(5):
    cantar_parabens()

# em python podemos inclusive criar variaveis do tipo de uma função e executar essa função atraves da variavel

canta = cantar_parabens
canta()