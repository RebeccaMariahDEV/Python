"""
POO - Propriedades - Propertis

Em linguagem de programação com em java, ao declarar atributos privados nas classes,
continuamos a criar metodos publicos para manipulação desses atributos, esses metodos
são conhecidos como getters e setters, onde os getters retornam o valor do atributo
e os setters alteram os valores dos mesmos.

Getters : @property
Setters : @nome(do getters).setter


# podemos criar assism, porem assim é comum em java

class Conta:
    contador = 0
    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        return f" Seu saldo é de: {self.__saldo}, Cliente : {self.__titular}"

    def deposito(self, valor):
        self.__saldo += valor

    def saque(self, valor):
        self.__saldo -= valor

    def transferencia(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    def get_numero(self):
        return self.__numero

    def get_titular(self): # metodo para manipular os atributos
        return self.__titular

    def set_titular(self, titular): # altera o valor do atributo, tem que pensar bem antes de usar
        self.__titular = titular

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite

    def get_saldo(self):
        return self.__saldo



"""
class Conta:
    contador = 0
    def __init__(self, titular, saldo, limite): # sempre criar os atributos de formas privadas
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property # são getters
    def limite(self):
        return self.__limite

    @limite.setter # setters
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def extrato(self):
        return f" Seu saldo é de: {self.__saldo}, Cliente : {self.__titular}"

    def deposito(self, valor):
        self.__saldo += valor

    def saque(self, valor):
        self.__saldo -= valor

    def transferencia(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    @property
    def valor_total(self):
        return self.__saldo + self.__limite





conta1 = Conta("Angela", 3000, 5000)
conta2 = Conta("João", 2800, 4300)

print(conta1.extrato())
print(conta2.extrato())

soma = conta1.saldo + conta2.saldo
print(f"A soma das contas é {soma}")

print(conta1.__dict__)
conta1.limite = 76543
print(conta1.__dict__)

print(conta1.valor_total)
print(conta2.valor_total)