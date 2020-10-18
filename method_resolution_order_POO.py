"""
POO - Method resolution order

MRO:
É a prdem de execulsão dos metodos, ou seja, quem sera execultado primeiro.

Em Python, podemos conferir a ordem de execulsão da ordem de 3 formas:
via propriedade da classe;
via metodo;
via help


"""
class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def comprimentar(self):
        return f" eu sou o {self.__nome}"

class Aquatico(Animal):

    def __init__(self, nome):
        self.__nome = nome

    def nadar(self):
         return f" {self._Animal__nome}"

    def comprimentar(self):
        return f" eu sou o {self._Animal__nome}"

class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f" {self._Animal__nome} esta andando"

    def comprimentar(self):
        return f" eu sou o {self._Animal__nome}"

class Pinguim(Terrestre, Aquatico):
    def __init__(self, nome):
        super().__init__(nome)

tux = Pinguim("tux")
print(tux.comprimentar())