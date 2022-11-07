'''
Escrevendo em arquivos

OBS: Ao abrir um arquivo para leitura, não podemos realizar a escrita nele
se abrirmos um arquivo para escrita, não podemos lê-lo

O argumento precisa ser STRING
Abrindo um arui


# modo w - write -> escrita
# AO abrir um arquivo para escrita um arquivo é criado no sistem operacional
with open('novo.text', 'w') as arquivo:
    arquivo.write('Escrever dados em arquivo é muito fácil.\n')
    arquivo.write('Podemos colocar quantas linhas quisermos')

with open('millinhas.txt', 'w') as arquivo:
    arquivo.write('Ray \n' * 100)


exemplo a:

with open('Frutas.txt', 'a') as arquivo_frutas:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo_frutas.write(fruta +'\n')
        else:
            break
'''


with open('outro.txt', 'a') as arquivo:
    arquivo.seek(0)
    arquivo.write('Nova linha\n')
    arquivo.write('Mais uma linha\n')