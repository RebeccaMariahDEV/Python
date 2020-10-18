"""
Funçoes de maior grandeza - Higher Order Fuunctions or HOF

Oque isso significa?!
- quando uma linguagem de programação suporta, ou seja, permite usar esse conceito,
indica que podemos ter funções que retornam outras funções como resultado ou
mesmo que podemos passar funções como argumentos para outras funções, e ate mesmo
criar variaveis do tipo de funções nos nossos programas.

OBS: na seção de funções nos utilizamos isso.

Em python as funções são cidadoes de primeira classe

# Exemplos- Definindo as funções
def soma(a, b):
    return a + b
def menos(a, b):
    return a - b
def mutiplicar(a, b):
    return a * b
def dividir(a, b):
    return a / b
def calcular(n1, n2, funcao):
    return funcao(n1, n2)

# teste de funções
print(calcular(4,8, soma))
print(calcular(4, 8, menos))
print(calcular(4, 8, mutiplicar))
print(calcular(4, 8, dividir))


"""
# Nested functions - funções aninhadas

"""
Em python podemos tambem ter funções dentro de funções
conhecidas como Nested Functions ou Inner functions (funções internas)

# exemplo

from random import choice # aleatorio

def comprimento(pessoa):
    def humor():
        return choice(("e ai?!", "sai daqui", "Gosto de você"))
    return humor() + pessoa

print(comprimento(" marcelo"))
print(comprimento(" cacau"))

# Retornando funções de outras funções
from random import choice
def faz_rir():
    def rir():
        return choice((" habahhahahahhah", "kkkkkkkkkk", " uahsduashduguifdguifguidsgf"))
    return rir()

rindo = faz_rir()
print(rindo)


"""
# Inner functions ou Nested functions, podem acessar o escopo de funções mais externa

from random import choice
def faz_me_rir(pessoa):
    def dando_risada():
        risada = choice((" hahahahaha", "kkkkkkk", "rsrsrsrsrs"))
        return f"{risada} {pessoa}"
    return dando_risada()
# teste
rindo = faz_me_rir(" marcelo ")
print(rindo)