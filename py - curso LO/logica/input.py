''' Entrada de dados em python'''

nome = input('Qual o seu Nome? ')
idade = input('Qual a sua idade? ')

ano_nasimento = 2022 - int(idade)

print(f'O usuário digitou {nome} e o tipo é {type(nome)}')

print(f'{nome} tem {idade} anos. Nasceu em {ano_nasimento}')


numero_1 = int(input('Digite um número'))
numero_2 = int(input('Digite outro número'))

print(numero_1 + numero_2)