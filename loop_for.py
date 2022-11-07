'''
Loop - estutura de repetição
for - uma dessas estruturas

for item in teravel:
	execução do loop

ultilizamos loops para iterar sobre sequencias ou sobre valores iteraveis
ex de iteraveis: 
- string
	nome = 'Geek university'
	nome[0] -> coloca na tela o 'G' - primeira letra, na posição 0
- lista
	lista = [1, 3, 5, 7, 9]
- Range
	numeros = range [1, 10]



#exemplo for 1 (iterando em uma string)
nome = 'DeuJogo.bet'
lista = [1,3, 5, 7, 9]
numeros = range(1, 10) #temos que tranformar em uma lista

for letra in nome:
	print(letra)

#exemplo for 2 (iterando sobre uma lista)

for numero in lista:
	print(numero)

#exemplo for 3 (interando sobre um range)
#range(valor_inicial, valor_final) 
#obs o valor é não inclusive - no exemplo abaixo vai ate o 9
for numero in range(1, 10):
	print(numero)

#enumerate: ((0, 'D'), (1, 'e')....)
for indice, letra in enumerate(nome):
	print(nome[indice])

for indice, letra in enumerate(nome):
	print (letra, end = '')

for valor in enumerate(nome):
	print(valor)

for n in range(1, qtd)
	print(f'imprimindo {n}')
	'''

qtd = int(input('quantas vezes rodar o loop?'))
soma = 0
for n in range(1, qtd+1):
	num = int(input(f'Informe o {n}/{qtd} valor :'))
	soma = soma + num
print (f'A soma é: {soma}')


#emoji
for num in range(1, 11):
	print('\U0001F60D' * num)
