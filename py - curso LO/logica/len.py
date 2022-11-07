''' Função len() Só funciona com String'''



usuario = input('Digite seu usuário: ')

if len(usuario) <= 10:
    print('Você foi cadastro no sistema')
    print('Quantidade de caracteres: ', len(usuario))
else:
    print('Usuário tem mais que tem 10 caracteres') 

## soma caracteres de strings

string1 = input('Digite alguma coisa')
string2 = input('Digite outra coisa')

print(f'A quantidade total de caracteres digitados foi: {len(string1) + len(string2)}')

