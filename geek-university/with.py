'''
O bloco with

passo para trabaçhar com arquivos:

1 - abrir o arquivo  -> open()
2 - manipulamos o arquivo  -> .read .readline()
3 - fechamos com arquivo -> close()

O block with é utilizado para criar um contexto de trabalhoo onde os recu
rsos utilizados são fechados após o bloco with

'''


with open('texto.txt') as arquivo:
    print(arquivo.readline())
    print(arquivo.closed)

print(arquivo.closed)

