"""
 - List Comprehensions
Oq é?!
Utilizando ele podemos gerar novas listas com dados processados apartir de outro interavel

# Exemplo de Sintaxe
[dado for dado in interavel]

"""

numeros = [1, 2, 3, 4, 5, 6]
res = [numero * 10 for numero in numeros]
print(res)
"""
Para entender melhor oq esta acontecendo vamos dividir ela em duas
1: for numero in numeros
2: numero * 10

"""
res = [numero / 2 for numero in numeros]
print(res)

def funcao(valor):
    return valor * valor
res = [funcao(numero) for numero in numeros]
print(res)

# Em loops
numeros = [1, 2, 3, 4, 5, 6]
numeros_dobrados = []
for numero in numeros:
    numeros_dobrados.append(numero*2)
print(numeros_dobrados)

# List comprehensions
print([numero * 2 for numero in numeros])

# outros exemplo
nome = "rebecca"
print([letra.upper() for letra in nome])

# exemplo 2
amigos = ["Antonio", "manuela", "vinicius", "carla"]
print([amigo.upper() for amigo in amigos])

# Exemplo 3
print([numero **2 for numero in range(1,10)])

# Exemplo 4
print([bool(valor) for valor in [0, [], "", True, 1, 3.14]])

# Exemplo 5
print([str(numero) for numero in [1, 2, 3, 4, 5, 6]])