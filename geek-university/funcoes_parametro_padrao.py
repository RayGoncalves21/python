'''
Funções com parâmetro padrão

funções onde a passagem parametro seja aopcional

'''

import re


print() # é opcional o parametro

def quadrado(numero):
    return  numero ** 2
print(quadrado(3)) # o 3 é o parâmetro obrigatorio

def exponencial(numero, potencia = 3):
    return numero ** potencia

print(exponencial(2)) # 2 *2 * 2 = 8
print(exponencial(2, 5))
# se o usuario passar apenas um parametro este será atribuido ao parametro numero, e será acalculado
# se o usuario passar dopis argumentos, o primeiro será atribuido ao parametro e o segundo ao parametro potencia

# em funções python, os parametros com valores default (padrao), sempre devem estar no final da declaração

# outros exemplos

# com o default num 1 e num2
def soma(num1 = 10, num2 = 20):
    return  num1 + num2
print(soma(4,3))
print(soma(4))
print(soma())

# type erros

def soma(num1, num2):
    return  num1 + num2
print(soma(4,3))
#print(soma(4)) # type error
#print(soma()) # type errror


# exemplo mais complexo

def mostra_informacao(nome = 'Geek', instrutor = False):
    if nome == 'Geek' and instrutor:
        return 'Bem vindo instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá, {nome}'

print(mostra_informacao())
print(mostra_informacao('Ray'))
print(mostra_informacao(instrutor=True))
print(mostra_informacao('Ray', instrutor=True))

def soma (num1, num2):
    return num1 + num2

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

def subtracao (num1, num2):
    return num1 - num2

print(mat(2, 3))
print(mat(2, 10, subtracao))


# escopo - evitar problemas e conslusões

# variaveis globais e locais, quando tiverem o mesmo nome será dado prioridade a local

total = 0
def incrementa():
    global total # avisndo que que queremos utilizar a variavel global

    total = total + 1
    return total

print(incrementa())

# podemos ter funções que são declaradas dentro de funções 



def fora():
    contador = 0
    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()
