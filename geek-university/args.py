'''
Args - o *args é um parametro como outro qualquer, isso significa que vocÊ
poderá chamar de qualquer coisa, desde que comece com *

#ex *x - 

O parametro args utilizado em uma função coloca os valores extras informados como entrada em uma tupla,
então desde já lembre-se que tuplas são imutaveis


def soma_todos_numero(num1, num2, num3):
    return num1 + num2 + num3

print(soma_todos_numero(4,6,9))
'''
# entendendo o args e facilitando

def soma_todos_numero(*args):
    return sum(args)

soma_todos_numero()
print(soma_todos_numero(1,3))
print(soma_todos_numero(2,3,4))
print(soma_todos_numero(2,3,4,5,6))
print(soma_todos_numero(2,3,4,5,6,25,65,84,65,325,6))


def verifica_info(*args):
    if 'geek' in args and 'university' in args:
        return 'Bem-vindo Geek'
    return 'Eu não tenho certeza quem é você'

print(verifica_info())
print(verifica_info(1, True, 'university', 'geek'))
print(1, 'university', 3.145)
