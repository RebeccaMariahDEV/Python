"""
Entendendo Iterators e Iterables

iterator -> um objeto de programação que pode ser iterado.
    - um objeto que retorna um dado sendo um elemento por vez, quando uma função next() é chamada

iterable -> um objeto que retornar um interator, quando a função iter() for chamada.

nome = "rebecca" # é um iterable mas não é um iterator
numeros = [1, 2, 3, 4, 5] # igual a str

it1 = iter(nome)
it2 = iter(numeros)
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
# se colocar next a mais do que tem dara erro StopIteration
# Isso é quase como um for


"""
numeros = [1, 2, 3, 4, 5]
nome = "rebecca"
for l in nome:
    print(f"{l}")
# utilizando o for, por baixo dos panos o python faz o next pra gente, sem dar erro
