''' Operadores lógicos 

and, or, not
in e not in
 '''

 # and = ambas devem ser verdadeiras (verdadeiro E falso) = False (verdadeiro E verdadeiro) = True
from traceback import print_tb


# scomparacao1 and comparacao2

 # or = uma deve ser verdadeira 
 # verdadeiro OU verdadeiro
# comp1 or comp2

 # not - inversão 

a = 2 
b = 3
# se não for verdadeiro
if not b > a:
    print('B é maior do que A')
else:
    print('A é maior do que B')

c = ''
d = 0

if not c:
    print('por favor preencha o valor de C')

# in e not in

nome = 'Rayzinho'
# tem a letra z no nome?
if 'z' in nome:
    print('Tem a letra')
else:
    print('Não tem a letra')

# se não tiver executa 
if 'fsdfsd' not in nome:
    print('executei (Não existe o texto)')
else:
    print('Exite o texto')


##############  Sistema de login ###########

usuario = input('Nome do Usuario: ')
senha = input('Senha do Usuário: ')

usuario_bd = 'ray'
senha_bd = '210595'

if usuario_bd == usuario and senha_bd == senha:
    print('Bem vindo')

else:
    print('Usuário ou senha inválidos, tente novamente')
