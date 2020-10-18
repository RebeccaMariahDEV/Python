"""
Decorators com diferentes assinaturas

# Relembrando
def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f" Olá eu sou {nome}"

@gritar
def ordenar(principal, acompanhamento):
    return f"Olá, gostaria de {principal} acompanhado com {acompanhamento} por favor"

# print(saudacao("rebecca"))
print(ordenar("costela", "batata"))

# Para resolver utilizamos o decorator pattern

# Refatorando
def gritar(funcao): # o nome e parametros da função é sua assinatura
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f" Olá eu sou {nome}"

@gritar
def ordenar(principal, acompanhamento):
    return f"Olá, gostaria de {principal} acompanhado com {acompanhamento} por favor"

print(saudacao("rebecca"))
print(ordenar("costela", "batata"))


"""

# Decorator com parametros
def verifica(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f"valor incoreto, primeiro argumento precisa ser um {valor}"
            return funcao(*args, **kwargs)
        return outra
    return interna

@verifica("pizza")
def comida(*args):
    print(args)

# @verifica(10)
# def soma(n1, n2):
#     return n1 + n2
# print(soma(9, 7)) # erro: valor incoreto, primeiro argumento precisa ser um 10
# print(soma(10, 7))

print(comida("pizza", "sushi"))
print(comida("lasanha"))