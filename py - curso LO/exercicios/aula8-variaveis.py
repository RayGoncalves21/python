
nome = str(input('Seu Nome'))
idade = int(input('Sua idade'))

altura = float(input('Sua altura'))
peso = float(input('Peso'))
ano_atual = 2022

ano_nascimento = ano_atual - idade

imc = peso / altura ** 2

print(f'{nome} tem {idade} anos. \nNascido em {ano_nascimento}. \nPesa {peso:.0f}Kg tem a altura de {altura} e o imc é: {imc:.2f}')
