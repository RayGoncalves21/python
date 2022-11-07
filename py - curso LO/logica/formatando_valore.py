'''
Formatando valores em modificadores

:s - texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NUMERO)f - quantidade de casas decimais (float)
:(CARACTERE) (> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - esquerda
< - Direita
^ - Centro
'''

num_1 = 10
num_2 = 3

divisao = num_1 / num_2

print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')

num_3 = 1

# numero 1    0 - acrescta zero  > - a esquerda  10- quantidade
print(f'{num_1:0>10}')


num_4 = 1150

print(f'{num_4:0^10}')


nome = 'Otavio Miranda'

print(f'{nome:#^50}')

nome_formatado = '{n:*^20}'.format(n=nome)
print(nome_formatado)

print(nome.lower())
print(nome.upper())
print(nome.title())