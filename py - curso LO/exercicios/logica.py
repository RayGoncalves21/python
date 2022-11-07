"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um número: ')

     # impar ou par

try:
    numero = float(numero)
    resto = numero % 2
    if resto == 0:
        print(f'{numero} é Par')
    else: 
        print(f'{numero} é Impar')

except:
    print('erro')

###### de outro jeito com isdigit() #######

numero_inteiro = input('Digite um numero inteiro')

if numero_inteiro.isdigit():

    numero_inteiro = int(numero_inteiro)

    if numero % 2 == 0:
        print(f'{numero_inteiro} é par')
    else:
        print(f'{numero_inteiro} é impar')
else:
    print('Isso não é um número inteiro.')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
    # De acordo com o horario

horario = input('Que horas são? ')

if horario.isdigit():
    horario = int(horario)

    if horario < 0 or horario > 23:
        print('Horário deve estar entre 0 e 23')
    elif horario <= 11:
        print('Bom dia')
    else: 
        print('Boa noite')
else:
    print('Por favor, digite um horario válido')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
#### caracteres 

nome = input('Digite seu Nome: ')

if len(nome) < 4:
    print('Nome curto')
elif len(nome) >=5 and len(nome) <=6:
    print('Nome normal')

elif len(nome) > 6:
    print('Nome muito grande')