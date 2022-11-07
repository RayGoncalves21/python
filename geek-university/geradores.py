'''
Geradores

    - Geradores são iterators (iteradores)
obs: o contrario não é verdadeiro, nem todo iterator é um generator
outras informações, generators, podem ser criado com funções geradoras
Funções gerddoras ultilizam a palavra reservada yield
generators podem sem criados com funções geradoras

Diferença entre funções e gerador functions (funçõpes geradoras)

-------------------------------------------
Fnções              | Generator Functions
--------------------|----------------------
Utilizam return     | Utilizam Yield
retorna uma vez     | Podem utilizar yield multiplas vezes
Quando executada    | quando executada retorna um generator
retorna um valor    |

'''

# exemplo de generator function

def conta_ate(valor_maximo):
    contator = 1
    while contator <= valor_maximo:
        yield contador
        contator = contator + 1

# OBS: uma generator Function não é um Generator. Ela gera um generator


gen = conta_ate(5):
