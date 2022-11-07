'''
Para o 'and', ambos precisam ser True
para o 'or', um ou outro precisa ser True
para o 'not', o valor do boolean é invertido, ou seja, se for true vira false - negação
para o 'is' 
'''

ativo = True
logado = True

if ativo and logado:
	print('Bem-vindo usuário')
else:
	print('Você precisa ativar a sua conta, por favor, cheque o seu e-mail.')	

print(not True)

if not ativo:
	print('Bem-vindo usuário')
else:
	print('Você precisa ativar a sua conta, por favor, cheque o seu e-mail.')

	print (ativo is False)