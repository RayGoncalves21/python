'''
De modo geral o range são ultilizados para gerar squencias numericas, de maneira especificiada.

formas gerais:

range(valor_parada)
obs: valor parada não inclusive (inicio padrao 0) sempre ele -1
'''
#forma 1
for num in range(11):
	print(num)

print()

#forma 2 

for num in range(100, 166):
	print(num)

print()
#forma 3 - passo expecificado pelo usuario

for num in range(150, 200, 5):
	print(num)

print()
#Forma 4 - inverse 
for num in range(10, -1, -1):
	print(num)



