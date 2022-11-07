class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None

    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    

class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

class MaquinaDeEscrever:
    def __init__(self, modelo):
        self.__modelo = modelo

    @property
    def modelo(self):
        return self.__modelo