"""
Modulo Random

Entendendo os Modulos em Python

- Em python, modulos nada mais são do que outros arquivos Python
- Modulo rando -> possuem varias funçoes para geração de numeros pseudos aleatorios.
OBS: existem duas formas de utilizar essa função.
# Importar todo o modulo não é recomendado.

- Random gera um numero pseudo aleatorio entre 0 e 1.

"""
# Forma 1

import random
"""
 # Ao realizar um import de todo modulo, todas as funções, atributos, propriedades que estiverem, ficaram em memoria
 dentro do modulo.
 OBS: caso vc saiba quais funções precisa utilizar desse modulo, essa não seria a formula ideal de utilizar
 
"""
print(random.random())
#OBS: para utilizar a func random do pacote, precisa do nome do pacote e o nome da função separados por ponto
# não confunda a função random com o pacote, pode parecer confunso mas a func é apenas uma das funções no modulo random

# Forma 2, importando uma função expesifica do modulo

from random import random
# No importe acima, estamos falando para importar apenas a função random do modulo random
# OBS: o importe não tem (), apenas na execução tem ()

# for i in range(10):
#     print(random())

"""
Para valores podemos usar a função uniform() que gera numeros pseudos aleatorios
Para isso deve fazer o importe da função no modulo random

"""
from random import uniform

# for i in range(10):
#     print(uniform(2, 7)) # o ultimo parametro não é incluido
# gera um numero real com parametros que voce define

"""
Para valores inteiros pseudos aleatorios entre os valores pasados como parametros.
Tem que importar do modulo rando o randint, é a utilização sera a mesma

"""
from random import randint

# for i in range(6):
#     print(randint(0, 89), end=",") # para separar com virgula e mostrar todos na mesma linha

"""
Choice() -> mostra valor aleatorio em um intervalo de inteiro
"""
jogadas = ["pedra", "papel", "tesoura"]

from random import choice
print(choice(jogadas))

# podemos tbm usar em str exemplo
print(choice("cacau"))# ele sorteia uma latra desse interavel

"""
Shuffle() tem a função de embaralhar dados
"""
from random import shuffle

cartas = ["as", "rei", "3", "dama", "6"]
shuffle(cartas) # emparalha os seus dados
print(cartas)
print(choice(cartas)) # retira um em sorteio
print(cartas.pop()) # retira o ultimo valor e te devolve
