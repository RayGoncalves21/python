''''
utilizamos o gerenciador de pacotes chamado pip - python installer package

pip install nome-do-modulo
https:\\pypi.org  - pacotes oficiais externos
from colorama import init
from colorama import Fore, Back, Style


# colorama -> é utilizado para permitir impressao de textos coloridos no terminal

init()
print(Back.BLACK + 'TMJ')
print(Fore.RED + 'Rayzinho')
print(Fore.CYAN + 'Deu Jogo')

'''
import pydf

pdf = pydf.generate_pdf('<h1>Ray</h1><br/><strong>Mestre do python</strong>')

with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)