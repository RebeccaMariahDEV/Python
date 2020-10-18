"""
POO - Metodos

- Metodos -> podemos chamar de funções, pois representam os comportamentos do objeto, ou seja,
as ações que este objeto pode realizar no seu sistema.

Em python dividimos os metodos em 2 grupos, o de instancias e o de classes.

# metodo de instancia
O metodo dunder init é um metodo especial chamado de construtor, e é
para inicializar a função.

OBS: Todo elemento em python que inicia e finaliza com duplo underline é chamado de dunder
Os metodos dunder em python são chamados de metodos magicos

ATENÇÂO: por mais que possamos criar nossas proprias funções com dunder no inicio e no fim,
não é aconselhado, por conta das funções internas do python, podendo assim modificar as funções
sem querer e alterando todo o programa
"""
class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

class ContaCorrente:
    contador = 1234

    def __init__(self, saldo, limite):
        self.__numero = ContaCorrente.contador + 1
        self.__saldo = saldo
        self.__limite = limite
        ContaCorrente.contador = self.__numero


class Produto:
    #atributo de classe
    imposto = 1.05 # 0.05% de impostos
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = valor * Produto.imposto
        Produto.contador = self.id

    def desconto(self, porcentagem):
        return (self.valor * (100 - porcentagem)) / 100

"""
p1 = Produto("ps4", "video game", 2300)
p2 = Produto("notebook", "computador", 4500)

print(p1.desconto(35)) # metodo de instancia
"""
from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:

    contador = 0

    @classmethod
    def conta_usuario(cls): # parametro propria classe
        print(f" Temos {cls.contador} usuarios no sistema")

    def __init__(self, nome, sobrenome, email, senha):
        self.id = Usuario.contador + 1
        self.email = email
        self.nome = nome
        self.__senha = cryp.hash(senha, rounds=20000, salt_size=6)
        self.sobrenome = sobrenome
        Usuario.contador = self.id

    def nome_completo(self):
        return f" {self.nome} {self.sobrenome}"

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

# user1 = Usuario("rebecca", "mariah", "user1@gmail.com", "24567")
# print(user1.nome_completo())
# print(Usuario.nome_completo(user1))

# nome = input("nome: ")
# sobrenome = input("sobrenome: ")
# email = input(" email: ")
# senha = input("senha: ")
# confirma_senha = input("confirme a senha: ")
#
# if senha == confirma_senha:
#     user = Usuario(nome, sobrenome, email, senha)
# else:
#     print("Senhas não batem")
#     exit(1)
#
#
# print("usuario criado com sucesso")
#
# senha = input("informe a senha para acesso: ")
#
# if user.checa_senha(senha):
#     print("Acesso permitido")
# else:
#     print("acesso negado")
#
# print(f" senha user criptografada: {user._Usuario__senha}")

"""
Metodos de classe
@classmethod
    def conta_usuario(cls): # parametro propria classe
        print(f" Temos {cls.contador} usuarios no sistema")
        
OBS: os metodos de instancia é feito quando precisamos acessar algum atributo de instancia,
já no metodo de classe não temos acesso a atributos, apenas a cls(classe)

OBS: metodos de classe em python são conhecidos como metodos estatico em outras linguaguens

"""
user = Usuario("rebecca", "mariah", "user1@gmail.com", "24567")
Usuario.conta_usuario() #forma correta, o acesso é via nome de classe
user.conta_usuario() # possivel porem não é correto
