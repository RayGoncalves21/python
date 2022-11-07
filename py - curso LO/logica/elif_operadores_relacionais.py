'''

Operadores relacionais

== Igual
> Maior que
>= Maior ou igual a
< menor que
<= menor ou igual a
!= Diferente

todas retornam valor booleano
'''

num_1 = 2
num_2 = 2
print(num_1 == num_2)

expressao = (num_1 > num_2)
print(expressao)

var_1 = 'Luiz'
var_2 = "Otávio"

expressao = (var_1 == var_2)

print(expressao),


expressao2 = (var_1 != var_2)

print(expressao2)


# emprestimo

nome = input('Qual o seu nome: ')
idade = int(input('Qual a sua idade? '))

# idade limite para pegat emprestimo
idade_menor = 20 # muito jovem
idade_maior = 40 # passou da idade

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo \o/')
else:
    print(f'{nome} NÂO pode pegar o empréstimo :(')

