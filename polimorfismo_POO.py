"""
POO - Polimorfismo

Poli -> muitas
Morfiis -> formas

Quando reimplementamos um metodo presente na classe pai em classes filhas
estamos realizando uma sobrescrita de metodos (Overriding)

O overriding é a essesncia do polimorfismo
"""
class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError( "A classe filha precisa implementar este metodo")

    def comer(self):
        print(f"{self.__nome} esta comendo...")

class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f"{self._Animal__nome} fala au au")

class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f"{self._Animal__nome} fala miau")

class Rato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

cacau = Gato("cacau")
print(cacau.falar())
print(cacau.comer())

rex = Cachorro("rex")
print(rex.falar())
print(rex.comer())

tom = Rato("tom")
print(tom.comer())
