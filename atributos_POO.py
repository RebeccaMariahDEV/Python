"""
POO:
    - Atributos -> representam as caracteristicas do objeto, ou seja, pelaos atributos
    nós conseguimos  representar computacionalmente os estados de um objeto


Em python dividimos os atributos em 3 grupos:
    - os de instancias
    - os de classes
    - os dinamicos

# Atributos de instáncia:
São atributos declarados dentro do metodo construtor,
OBS: metodo construtor é um metodo especial utilizado para a construção de um objeto

# Dica, esse self foi elaborado e utilizado pela convenção de programadores python
# porem você pode utilizar qualquer nome

Em Python ficou estabelecido por convenção que todo atributo de uma classe é publico,
ou seja, pode ser acessado em todo o projeto.
Caso queiramos demonstrar que determinado atributo deve ser tratado como privado,
ou seja, que deve ser acessado e utilizado somente dentro dessa classe onde está
declarado, utilizasse duplo __ no inicio do nome.

Isso é conhecido tambem como Name Mangling

Em python, ele não obriga a utilizar variaveis privadas como atributos,
ele funcionara normalmente, porem por segurança você pode utilizar o privado.


"""
# Classes com atributos de instancia publica

class Lampada:

    def __init__(self, voltagem, cor):# __init__ é o metodo construtor
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False

class ContaCorrente:

    def __init__(self, saldo, limite, numero):
        self.saldo = saldo
        self.limite = limite
        self.numero = numero

# class Produto:
#
#     def __init__(self, nome, descricao, valor):
#         self.nome = nome
#         self.descricao = descricao
#         self.valor = valor

class Usuario:

    def __init__(self, nome, email, senha):
        self.email = email
        self.nome = nome
        self.senha = senha

class Acesso:

    def __init__(self, email, senha):
        self.__email = email
        self.__senha = senha

    def mostra(self):# modo correto
        print(self.__senha)
        print(self.__email)

#OBS: lembrece que isso é apenas uma convenção, a linguagem não impede que façamos
# acessos a atributos privados fora da classe

# Exemplo
user = Acesso("user@gemail.com", "12345")
# print(user.__email) #AttributeError quando o acesso é errado
# Correto é, para atributos privados
# print(user._Acesso__email) # name mangling
#
# # Modo correto
# user.mostra()

"""
Atributos de instancia:
- significa que ao criarmos instancias/objetos de uma classe todas as instancias
terão esse atributo.

# Atributos de classe
- São atributos que são declarados diretamente na classe, ou seja, fora do construtor,
geralmente já inicializamos um valor, e esse valor é compartilhado entre todas as instancias da classe
Ao insves de cada instancia da classe ter seus proprios valores, como é o caso dos atributos de instancias,
com os atributos de classes, todas as instancias terão o mesmo valor desse produto

Atributos dinamicos:
- Ele nada mais é do que um atributo que pode criado em tempo de execulção
OBS: o atributo dinamico sera exclussivo da instancia que o criou

"""

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


p1 = Produto("ps4", "video game", 2300)
p2 = Produto("notebook", "computador", 4500)

# print(p1.valor) # Acesso possivel mas incorreto
# print(p2.valor)
# # Não precisamos criar uma instancia de uma classe para fazer acesso a um atributo de classe
#
# print(Produto.imposto) # Acesso correto de um atributo de classe
#
# #
# print(p1.id)
# print(p2.id)

# Criando um atributo dinamico em tempo de execulção
p2.peso = "2kg" # a classe produto não existe o pesso
print(f" Poduto {p2.nome}, Descrição {p2.descricao}, Valor {p2.valor}, peso {p2.peso}")
# Podemos criar um novo atributo que só existira para u produto que foi criado

# Deletando atributos dinamicamente
print(p1.__dict__) # mostra a propriedade dentro da variavel, mostrando como em um dicionario
del p2.peso
print(p2.__dict__)