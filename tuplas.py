"""
# cuidado, as tuplas sao representadas por parentes
tupla1 = (1, 2, 3, 4, 5, 6)
print(type(tupla1))
tupla2 = 1, 2, 3, 4, 5, 6
print(type(tupla2))
a = 1, 2, 3, 4, 5, 6
print(type(a))

# cuidado 2
tupla3 = (4) # isso nao é uma tupla
print(type(tupla3))

tupla4 = (4, )
print(type(tupla4))
# podemos concluir que tuplas sao definidas por (,) e nao por parenteses
# Nao pode esquecer que para ser Tupla tem q colocar o elemento e depois uma Virgula

# podemos gerar uma tupla dinamicamente com o range
tupla = tuple(range(11))
print(tupla)

# Desempacotamento de tupla
tupla = ("Rebecca", "marcelo", "cacau")
mozao, mozi, pet = tupla
print(mozao, pet)
print(mozi)

#Nao existe metodo de adicao nas tuplas, por serem imutaveis

#porem metodos de soma, maximo, minimo, e tamanho funciona apenas com numeros reais ou inteitos
tupla = 1, 2, 3, 4, 5, 6,

print(sum(tupla))
print(max(tupla))
print(min(tupla))

# Ja mistura de valores, funciona apenas o len
tupla = 1, 2, 3, 4, 5, 6, "b"
print(len(tupla))

# Concatenar
tupla1 = 1, 2, 3,
tupla2 = 4, 5, 6,
print(tupla1 + tupla2) # tuplas sao imutaveis
print(tupla1)
print(tupla2)
tupla3 = tupla1 + tupla2
print(tupla3)

# Caso queira colocar todos os valores sem criar uma nova tupla, tem como sobrescrever uma tupla
tupla1 = tupla1+tupla2
print(tupla1)

# Podemos verificar se tem determinado elemento em uma tupla assim como em listas:
tupla = 1, 2, 3, 4, 5, 6,
print(3 in tupla)

# Interando sobre uma tupla

tupla = 1, 2, 3, 4, 5, 6,
for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# contando elementos dentro de uma tupla
tupla = ("a", "b", "c", "d", "a", "b")
print(tupla.count("c"))

# Transformando str em tuple
tupla = ("a", "b", "c", "d", "a", "b")
mozoes = tuple("mussi e cacau")
print(mozoes.count("c"))

tupla = ("a", "b", "c", "d", "a", "b")
# dicas de utilizar tuplas
#Devemos utilizar tuplas Sempre que nao precisarmos modificar os dados contidos em uma coleção
# Exemplo 1

meses = ("janeiros", "fevereiro", "marco", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro")
print(meses)

# O acesso a elementos de uma tupla, tambem é semelhante a de uma lista
print(meses[5])

# Interando com o While
i = 0
while i < len(meses):
    print(meses[i])
    i += 1
print(meses[: : 2])
# OBS caso o elemento nao exista aparecera erro

# Copiando uma tupla para outra
# em tuplas nao temos o problema de Shallow copy
tupla = ("janeiros", "fevereiro", "marco", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro")

nova = tupla
print(nova)
print(tupla)
outra = 1, 2, 3, 4,
nova += outra
print(nova)
print(tupla)
print(outra)

# Os metodos de tuplas são pequenos devido a tuplas serem imutaveis
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__'
, '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__si
zeof__', '__str__', '__subclasshook__', 'count', 'index']

"""



