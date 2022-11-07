'''
Sistema de aquivos e navegação

Para fazer uso de manipulação precisamos importar o os

os -> sistem operacional
'''

#fazer import

import os
# getcwd()-> Pega o currrent work directory - diretorio de trabalho corrente
# retorna o path (caminho) absoluto
print(os.getcwd()) # c:\Users\PC 1\Documents\1\python\novos

# para mudar o diretorio podemos usar o chdir()

os.chdir('..')

print(os.getcwd()) # c:\Users\PC 1\Documents\1\python

os.chdir('..')

print(os.getcwd()) # c:\Users\PC 1\Documents\1

# usar duas barras

print(os.path.isabs('c\\user\\pc1'))


# join  - acrescenta a pasta

# ele recebe dois parametro o primeiro o diretorio atual e o segundo o diret'orio que sera juntado ao atual

res = os.path.join(os.getcwd(), 'geek')

os.chdir(res)

print(os.getcwd())

# listando os arquivos e diretorios com o listdir()

print(os.listdir('C:\\'))