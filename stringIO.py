'''
String Io

ATENÇÂO: para ler e escrever dados do sistema operacional o sftware precisa ter permissão
    - Permissão de leitura para ler o arquivo
    - permissão de escrita para escrever o arquivo

Utilizado para ler e criar arquivos em memoria


'''

# primeiro fazemos o importe

from io import StringIO

mensagem = 'essa é apenas uma string normal'

# podemos criar um arquivo em memória já com uma string inserida ou mesmo vazio para insermos depois

arquivo = StringIO(mensagem)
# arquivo = open(arquivo.text, 'w')
# agora tendo o arquivo podemos utilizar tudo que já sabemos

print(arquivo.read())

# podemos movimentar o cursor