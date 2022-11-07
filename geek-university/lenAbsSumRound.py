'''
Len, abs, sum e round

Len() -> retorna o tamanho, ou seja, o número de itens de um iterável
abs() -> retorna o valor absoluto de um numero inteiro ou real, de forma basica seria o seu valor real sem o sinal
retorna tudo positivo, não funciona como string

# sum
sum() -> recebe como parâmetro um iterável, podendo receber um valor inicial e retorna a soma total dos elementos incluindo o valor inicial
#obs: o valor inicial default é 0
não funciona com strings

# ROUND
round() -> retorna um numero arredondado para N digito de precisão - DEFAULT o iteiro mais próximo
'''

# len
print(len('Geek University'))
print(len([1, 2, 3, 4, 5, 6, 7]))


# abs

print(abs(-5))
print(abs(-5))
print(abs(2.65))


# sum
print(sum([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5], 5))


# ROUND

print(round(10.2))
print(round(10.5))
print(round(10.5))
print(round(1.21212121212121, 2))
print(round(1.2999999, 3))
print(round(1.7999999))