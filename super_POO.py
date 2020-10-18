"""
POO - o metodo super()

O metodo super() se refere á classe super


"""
class Animal:
    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f"O {self.__nome} fala {som}")

class Gato(Animal):
    def __init__(self, nome, especie, raca):
        #Animal.__init__(self, nome, especie) possivel mas não recomendado
        super().__init__(nome, especie) # faz acesso a qualquer elemento da classe pai
        self.__raca = raca

felix = Gato("Felix", "felino", "Angora")

felix.faz_som("miau")
