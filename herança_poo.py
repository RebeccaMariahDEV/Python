"""
POO - Herança (Ibheritance)

A ideia de herança é reaproveitar codigos, tambem extender nossas classes

OBS: Com a herança a partir de uma classe existente nos extendemos outra classe
que passa a herdar atributos e metodos da classe herdada.

Cliente
    - nome
    - sobrenome
    - cpf
    - renda

funcionario do banco
    - nome
    - sobrenome
    - cpf
    - matricula

Existe alguma entidade generica o suficiente para encapsular os atributos e metodos comuns
a outras entidades???

OBS: quando uma classe herda de outras classe, ela herda todos os atributos e metodos da classe herdada

Quando uma classe herda de outra classe, a classe herdada é conhecida como por:
    - Super classe:
    - Classe mãe
    - Classe Pai
    - Classe base
    - Classe generica
Quando uma classe herda de outra classe ela é chamada:
    - Sub classe
    - Classe filha
    - Classe expecifica


class Pessoa: # é a super classe
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f"{self.__nome} { self.__sobrenome}"


class Cliente(Pessoa):
    # Cliente vai herdar os dados de Pessoa
    def __init__(self, nome, sobrenome, cpf, renda):

        self.__renda = renda
        super().__init__(nome, sobrenome, cpf) # metodo para acessar os dadaos da super classe


class Funcionario(Pessoa):
    # Funcionario vai herdar os dados de Pessoa
    def __init__(self, nome, sobrenome, cpf,  matricula):

        self.__matricula = matricula
        super().__init__(nome, sobrenome, cpf)

Sobrescrita de metodos (Overridig)

Sobrescrita de metodos, ocorre quando reescrevemos um metodo presente na super classe
filhas



"""
class Pessoa: # é a super classe
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f"{self.__nome} { self.__sobrenome}"


class Cliente(Pessoa):
    # Cliente vai herdar os dados de Pessoa
    def __init__(self, nome, sobrenome, cpf, renda):

        self.__renda = renda
        super().__init__(nome, sobrenome, cpf) # metodo para acessar os dadaos da super classe


class Funcionario(Pessoa):
    # Funcionario vai herdar os dados de Pessoa
    def __init__(self, nome, sobrenome, cpf,  matricula):

        self.__matricula = matricula
        super().__init__(nome, sobrenome, cpf)

    def nome_completo(self):
        print(super().nome_completo())
        return f"Matricula : {self.__matricula} nome : {self._Pessoa__nome}"




cliente1 = Cliente("rebecca", "mariah", "347.908.987-67", 2000)
funcionario1 = Funcionario("arthur", "nogueira", "567.876.874-89", 5643)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())
