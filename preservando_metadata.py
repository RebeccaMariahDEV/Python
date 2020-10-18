"""
Preservando metadatas com wraps

Metadatas -> são dados intrisecos em arquivos

Wraps -> são funções que envolvem elementos com diaversas finalidades.

# problema
def ver_log(funcao):
    def logar(*args, **kwargs):
         Eu sou a função (logar) dentro de outra
        print(f"Você esta chamando a {funcao.__name__}")
        print(f"aqui é a documentação {funcao.__doc__}")
        return funcao(*args, **kwargs)
    return logar

@ver_log
def  soma(a, b):
      Soma dois numeros
    return a + b

print(soma.__name__)
print(soma.__doc__)

"""

# Resolução do problema

from functools import wraps

def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """ Eu sou a função (logar) dentro de outra"""
        print(f"Você esta chamando a {funcao.__name__}")
        print(f"aqui é a documentação {funcao.__doc__}")
        return funcao(*args, **kwargs)
    return logar

@ver_log
def  soma(a, b):
    """ Soma dois numeros"""
    return a + b

print(soma(10, 78))

# print(soma.__name__)
# print(soma.__doc__)

