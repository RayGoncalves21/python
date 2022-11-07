'''
Modos de abertura de arquivo

r -> Abre para leitura - padrão
W -> Abre para escrita - Sobrescreve caso o arquivo já exista
x -> Abre para escrita somente se o arquivo não existir - se o arquivo existir ele dar FileExistError
a -> Abre para escrita e acrescenta caso já exista o arquivo - SEMPRE ao final do arquivo - não controlamos o cursor
+ -> abre para o modo de atualização, leitura e escrita - um arametro a mais ex: a+, r+, w+

exemplo x :

try:
    with open('university.txt', 'x') as arquivo:
        arquivo.write('Teste de conteudo\n')
except FileExistsError:
    print('Arquivo ja existe')

# exemplo a


with open('Frutas.txt', 'w') as arquivo:
    while True:
        fruta = input('Digite uma fruta ou sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break




'''

