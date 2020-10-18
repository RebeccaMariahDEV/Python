"""
POO - Abstração e encapsulamento

O grande objetivo da programação orientada a objetos é encapsular nossa codigo
dentro de um grupo logico e hierárquico utilizando classes.

# Relembrando Atributos/Metodos privados em python
Imagine que temos uma classe chamada pessoa
contendo um atributo privado chamado __nome e um metodo privado
chamado __falar()
Esses elementos privados só devem ser acessados dentro da classe,
porem o python não bloqueia o acesso fora da classe. Com python
acontece um fenomeno chamado name mangling, que faz uma alteração
na forma de ser acessado o elemento privado, conforme:

_Classe__elemento

Exemplo: acessando elementos privados fora da classe

instancia._Pessoa__nome
instacia._Pessoa__falar()

Abstração em POO é o ato de expor apenas dados relevantes de uma classe,
escondendo atributos e metodos privados do usuario.

"""

class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__saldo = saldo
        self.__titular = titular
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f" saldo do {self.__saldo} do titular {self.__titular} com limite de {self.__limite}")

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor
        if self.__saldo >= valor:
            self.__saldo -= valor
        else:
            print("saldo insuficiente")

    def transferir(self, valor, conta_destino):
        # 1 remover o valor da conta de origem
        self.__valor -= valor

        # 2 conta de origem
        conta_destino.__saldo += valor

conta1 = Conta("rebecca", 2400, 1000)
# print(conta1.titular)
# print(conta1.saldo)
# print(conta1.limite)
print(conta1.__dict__)
conta1.depositar(150)
print(conta1.__dict__)
conta1.sacar(450)
print(conta1.__dict__)
conta1.extrato()
conta2 = Conta("marcelo", 3500, 5700)
conta2.transferir(150, conta1)
print(conta1.__dict__)
print(conta2.__dict__)