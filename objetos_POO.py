"""
Poo - Objetos

Objetos são instancias da classe, apos o mapeamento do objeto do mundo real para sua
representação computacional, devemos poder criar quantos objetos forem nescessarios,
podemos pensar nos objetos/instancias de uma classe como variaveis do tipo definido na classe

"""
class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checar_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True

class ContaCorrente:
    contador = 1234

    def __init__(self, saldo, limite):
        self.__numero = ContaCorrente.contador + 1
        self.__saldo = saldo
        self.__limite = limite
        ContaCorrente.contador = self.__numero

class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.email = email
        self.nome = nome
        self.senha = senha
        self.sobrenome = sobrenome

# instancia do objeto
lamp1 = Lampada("branca", 220, 60)
print(f"A lampada esta ligada {lamp1.checar_lampada()}")
lamp1.ligar_desligar()
print(f"A lampada esta ligada {lamp1.checar_lampada()}")

cc1 = ContaCorrente(5000, 10000)

user1 = Usuario("rebecca", "mariah", "rebecca@gmail.com", "123456")

