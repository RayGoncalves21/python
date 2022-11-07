
primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

primeiro_valor = int(primeiro_valor)
segundo_valor = int(segundo_valor)

if primeiro_valor >= segundo_valor:
    print(
        f'O Primeiro valor = "{primeiro_valor}" é maior ou igual ao segundo valor="{segundo_valor}"')

else:
    print(
        f'O segundo valor="{segundo_valor}" é maior que o primeiro valor = "{primeiro_valor}"')
