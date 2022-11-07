'''
Sistema de arquivos - Manipulação


'''
import os
# decobrindo se um arquivo ou diretorio existe

print(os.path.exists('arquivo.txt')) # false
print(os.path.exists('Frutas.txt')) # true

# diretorio
print(os.path.exists('c:\\Users\\PC 1\\Documents\\1\\python'))

# Criando arquivos
# forma 1
open('arquivo.teste.txt', 'w').close()

# forma 2
with open('arquivo.teste2.txt', 'w') as arquivo:
    pass

# mlehor forma

os.mknod('arquivo-teste3.txt')
os.mknod('c:\\Users\\PC 1\\Documents\\1\\python\\teste4.txt')

# criando diretorios

os.mkdir('templates')
os.mkdir('templates\\geek')
os.mkdir('templates\\geek\\university')

# varios diretorios de uma vez

os.makedirs('templates\\geek\\university', exist_ok=True)