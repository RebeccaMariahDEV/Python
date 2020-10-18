"""
Modulo Built-in

Que são modulos integrados, que já estao no Python

|Python|modulos builtin|

# utilizando alias ( apelidos) para modulos ou funções

import random as rdm # não executa mais o random apenas o rdm(apelido)
print(rdm.random())

# Importando funções com *

from random import *
print(random())
# dessa forma, para utilizar é só usar a função do modulo

# Importando todo o modulo

import random
print(random.random())

# Apelidos para funções

from random import randint as rdi, random as rdm #importando duas funções
print(rdi(0, 89))
print(rdm())
# OBS: importante nao dar apelidos com nomes de funções ou variaveis etc

"""
from random import randint, random,shuffle,choice
#para importar mutiplas funções utilize tuplas para facilitar melhor a melhor comprienção
"""
Exemplo

from random import (
    random,
    choice,
    randint
    )

OBS: lembre de importar oq realmente é nescessario
    
"""
print(random())
print(randint(2,8))
print(choice("cacau"))
lista = [1, 2, 3, 4, 5, 6, 7]
shuffle(lista)
print(lista.pop())

