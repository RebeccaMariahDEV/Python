"""
List in dict

Pense assim:
Se queremos criar algo como lista, tupla, set ou dict faremos:
- lista [1, 2, 3, 4, 5, 6]
- tupla (1, 2, 3, 4, 5, 6)
- set {1, 2, 3, 4, 5, 6}
- dict {"a": 1, "b": 2, "c":3}

Sintxy é:
{chave: valor for valor in interavel}

"""
# Exemplo:
numeros = {"a": 1, "b": 2, "c":3, "d":4}
quadrado = {chave: valor **2 for chave, valor in numeros.items()}
print(quadrado)

# Lembra que em um dict nao tem repeticao de chave

chaves = "abcde"
valores = [1,2,3,4,5]
mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)

# Exemplo com logica condicional
numeros = [1,2,3,4,5,6,7,8,9]
res = {num:("par" if num % 2 == 0 else "impar")for num in numeros}
print(res)

"""
Para criar dict comprehensions e so utilizar {}, para lista o os []
Sets comprehensions
"""
# Exemplo
numeros = {num for num in range(1,8)}
print(numeros)
numeros = {x **2 for x in range(10)}
print(numeros)

# Faça uma alteração na estrutura acima, para gerar um dict
numeros = {x: x **2 for x in range(10)}
print(numeros)

letra = {letra for letra in "Rebecca"}
#cria um conjunto sem ordenação e sem repetição
print(letra)