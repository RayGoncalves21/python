'''
FUncoes com parametros de entrada
- funções que recebem dados para serem processados dentro da mesma;

Entrada -> processamento -> saída

se a gente pensr em uma função, já sabemos que temos funções que:
 	-não possuem esntrara
	- não possuem saída
	- possuem entrada mas não possuem saída
	- não possuem entrada mas possuem saída

'''

#refatorando uma função

def quadrado(numero):
    return numero * numero

print(quadrado(7))
print(quadrado(2))
print(quadrado(5))
'''
aniversariante = input('nome do Aniversariante: ')
def cantar_parabens():
    print('Parabéns pra você')
    print('Nessa data querida')
    print(f'felicidades {aniversariante}')
print(cantar_parabens())

'''

def cantar_parabens(aniversariante):
    print('Parabéns pra você')
    print('Nessa data querida')
    print(f'felicidades {aniversariante}')

cantar_parabens('Patricia')

# funcções podem ter n parametros de entrada, podemos receber como entrada em uma função, quantos parametros forem necessários, eles são separados por virgula


# exemplo

def soma (a, b):
    return a + b

def multiplica(num1, num2):
    return num1 * num2

def outra(num1, b, mensagem):
    return (num1 + b) * mensagem

print(soma(2, 5))
print(soma(10, 20))

print(multiplica(4, 5))
print(multiplica(2, 8))

print(outra(3, 2, 'test'))
print(outra(15, 18, 'pyhton - '))

# nomeando parametros

def nome_completo(nome, sobrenome):
    return f'Seu nome completo é: {nome} {sobrenome}'

print(nome_completo('Angelina', 'Jolie'))

# diferença entre parametros e argumentos

# parametros são variaveis declaradas na definição de uma função
# argumentos são dados passados durante a execução de uma função

# ordem dos parametros importa

# argumentos nomeados *keyword arguments

# erro comum na utilização do return

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total

lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))