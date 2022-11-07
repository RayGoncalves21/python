'''
Modulo colections - Counter

Conhecido por -> high perfomance container types

counter -> Recebe um interável como parametro e cria um objeto do tipo collections counter
que é parecido com um dicionario, contendo como chave o elemento da lista passada como paramentro
e como valor a quantidade de occorencia desse elemento
'''

# Realizando o import

from collections import Counter

#podemos utilizar qualquer iteravel, aqui usamos uma lista
lista = [1,1,2,2,3,3,1,1,1,2,2,4,4,4,5,5,5,3,42,66,43,34]


#utilizando o counter
res = Counter(lista)

print(type(res))
print(res)
# Counter({1: 5, 2: 4, 3: 3, 4: 3, 5: 3, 42: 1, 66: 1, 43: 1, 34: 1})
# para cada elemento da lista, o counter criou uma chave e colocou como valor a quantidade de ocorrencias

#   exemplo 2 - string
print(Counter('DeuJogo.bet'))


# exemplo 3

texto = '''William Feiner SJ (Münster, 27 de dezembro de 1792 – Washington, D.C., 9 de junho de 1829) foi um padre católico alemão e jesuíta que foi missionário nos Estados Unidos e, finalmente, o presidente da Universidade de Georgetown.

Nascido em Münster, ele ensinou em escolas jesuítas no Império Russo e na Galícia polaca como um jovem membro da Companhia de Jesus. Ele então emigrou para os Estados Unidos vários anos após a restauração da Sociedade, assumindo o trabalho pastoral e ensinando teologia em Conewago, Pensilvânia, antes de se tornar professor em tempo integral na Universidade de Georgetown. Lá, ele também tornou-se o segundo bibliotecário dedicado da biblioteca de Georgetown. Finalmente, Feiner tornou-se presidente da universidade em 1826. Enquanto presidente, ele ensinou teologia em Georgetown e ministrou à congregação na Igreja da Santíssima Trindade.

Apesar de ser o líder de uma universidade americana, ele nunca dominou a língua inglesa. Durante muito tempo atormentado por problemas de saúde devido à tuberculose, a sua curta presidência chegou ao fim depois de três anos, poucas semanas antes da sua morte.

Juventude
A brick church surmounted by a white tower, then a short grey steeple
Basílica de Conewago
Wilhelm Feiner nasceu no dia 27 de dezembro de 1792, na cidade de Münster, no principado-bispado de Münster (na actual Alemanha).[1][2] Ele entrou na Companhia de Jesus a 12 de julho de 1808, na Rússia Branca[3] (ou seja, Bielorrússia),[4] tornando-se oficialmente membro no dia 7 de agosto daquele ano.[5] Antes de emigrar para os Estados Unidos, ele ensinou em escolas jesuítas na Galícia polaca e no Império Russo,[1][6] onde os jesuítas foram autorizados a operar apesar de terem sido reprimidos pelo papa e expulsos da Europa Ocidental.[7] Por esse motivo, ele às vezes era erroneamente identificado como polaco e não como alemão.[1]

Missionário na América
Feiner foi enviado para os Estados Unidos em 1822 para ajudar os jesuítas americanos a restabelecer o seu trabalho após a restauração mundial da Companhia de Jesus em 1814.[8][9] Depois da sua mudança, ele anglicizou o seu nome para William Feiner.[1][2] De 1823 a 1826 ele foi designado assistente de Matthew Lekue na Basílica de Conewago na cidade de Conewago, condado de Adams, Pensilvânia,[10][11] onde havia uma grande comunidade de língua alemã.[12] Além do seu trabalho pastoral, Feiner ensinou teologia em Conewago em 1824.[13] Peter Kenney, o visitante jesuíta dos Estados Unidos, voltou à Europa e nomeou Feiner para o cargo no seu lugar; nesta altura Feiner já estava com a saúde muito debilitada,[14] sofrendo de tuberculose.[8]

Feiner foi gestor de estudos na Universidade de Georgetown no Distrito de Columbia de 1825 a 1826,[15] período durante o qual também serviu como professor de teologia e alemão.[16] James A. Neill assumiu como gestor no final do seu mandato.[17] Em 1825, Feiner tornou-se o segundo bibliotecário oficial da Biblioteca da Universidade de Georgetown quando Thomas C. Levins, que ocupava o cargo desde 1824, foi demitido da Companhia de Jesus e partiu para a cidade de Nova York. Quando Feiner deixou o cargo em 1826, James Van de Velde sucedeu-o.[18]

Presidente da Universidade de Georgetown
A pen-and-ink drawing of two large multi-storey buildings with many windows
Campus da Universidade de Georgetown em 1829
Quando o presidente da Universidade de Georgetown, Stephen Larigaudelle Dubuisson, teve permissão para renunciar ao cargo, ele ansiosamente viajou para a Europa.[19][20] Assim, Feiner foi nomeado presidente a 4 de maio de 1826[3] pelo superior provincial dos jesuítas, Francis Dzierozynski. Ele assumiu o cargo no dia 8 de julho de 1826,[21] apesar de sofrer de tuberculose avançada e de ser incapaz de falar até mesmo o inglês básico;[22] na verdade, ele nunca dominou a língua inglesa.[23] Quando soube da ordem do provincial, ele teria entrado no quarto de Dubuisson soluçando e declarando que não era competente para ocupar o cargo nem desejoso dele.[22] Enquanto presidente, Feiner ministrou à congregação na Igreja da Santíssima Trindade em Georgetown.[8] Ele também trabalhou como professor de teologia moral em 1828 e de teologia dogmática em 1829.[24]

Devido à saúde debilitada de Feiner, John W. Beschter deixou Baltimore para ir para a faculdade, prevendo que teria que suceder Feiner como presidente.[25] Dois historiadores da universidade, John Gilmary Shea e Robert Emmett Curran, consideraram a administração de Feiner, como outras da década, sem brilho.[26][21] Ele renunciou ao cargo a 30 de março de 1829[27] e faleceu na Universidade de Georgetown no dia 9 de junho daquele ano.[1]'''

print(Counter(texto))
print(texto)

#por palavra

palavras = texto.split()
res = Counter(palavras)
print(res)

# os 5 maiores: 
print('maiores occorencias', res.most_common(5))
