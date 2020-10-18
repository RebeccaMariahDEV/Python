"""
Modulo Collections: Named Tuple

# Tupla simples
tupla = 1, 2, 3,
print(tupla)

Named Tuple -> São tuplas diferenciadas onde especificamos um nome para ela e parametro,


"""
# Import
from collections import namedtuple

#Defininfo nome e parametro

#forma 1, declarando namedtuple
dog = namedtuple("Dog", "idade raça nome" )

# Forma 2, declarando namedtuple
dog = namedtuple("Dog", "idade, raça, nome")

#Forma 3, declarando namedtuple
dog = namedtuple("Dog", ["idade", "raça", "nome"])

# Como utilizar
ray = dog(idade=6, raça="pastor", nome="Thor")# ray é só uma variavel para receber os dados
print(ray)
print(ray[0]) # idade
print(len(ray))

# Acesso forma 1
print(ray.idade)
print(ray.nome)
print(ray.raça)

# Forma 2
print(ray.index(6))
print(ray.count("Thor"))

