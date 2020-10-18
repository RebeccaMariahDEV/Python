"""
POO - Herança multipla

Herança multiplas nada mais é do que a possibilidade de uma classe herdar de multiplas classes,
fazendo com que a classe filha herde todos os atributos e metodos de todas as classes herdadas

OBS: a herança multipla pode ser feita de duas maneiras:
- por multiderivação direta.
ou
- por multiderivação indireta.

# multiderivação direta
class Base1:
    pass

class Base2:
    pass

class Multiderivada(Base1, Base2): # pode colocar quantas quiser, não existe limites em python
    pass

# Exemplo 2 - multiderivação indireta

class Base1:
    pass

class Base2(Base1):
    pass

class Base3(Base2):
    pass

class Multiderivada(Base3):
    pass

OBS: não importa se a derivação é indireta ou não. A classe que realizar a herança herdara
todos os atributos e metodos das super classes.

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
        return f" eu sou o {self._Animal__nome} do mar"

class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f" {self._Animal__nome} esta andando"

    def comprimentar(self):
        return f" eu sou o {self._Animal__nome} da terra"

class Pinguim(Terrestre, Aquatico):
    def __init__(self, nome):
        super().__init__(nome)

# baleia = Aquatico("Wally")
# print(baleia.nadar)
# print(baleia.comprimentar)

tatu = Terrestre("Joca")
print(tatu.andar)
print(tatu.comprimentar())

# tito = Pinguim("tito")
# print(tito.andar)
# print(tito.nadar)
# print(tito.comprimentar())

# objeto de instancia
print(f" joca é instancia de terreste ? {isinstance(tatu, Terrestre)}")
print(f" joca é instancia de animal? {isinstance(tatu, Animal)}")
print(f" joca é instancia de aquatico?  {isinstance(tatu, Aquatico)}")
print(f" joca é instancia de pinguim ? {isinstance(tatu ,Pinguim)}")
print(f" joca é instancia de objeto? {isinstance(tatu, object)}")