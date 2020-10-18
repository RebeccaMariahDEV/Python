"""
Reversed

OBS: não confunda com a função reverse que estudamos em listas

Já a função reversed() funciona com qualquer interavel.
Sua função é inverter o interavel
OBS: tipos de objetos q retorna, a função retorna um interavel chamado list reverse iterator

"""
# Exemplo
lista = [1,2,3,4,5]
res = reversed(lista)
print(res)
print(type(res))

#podemos converter o elemento para uma tupla, lista ou set

# exemplo:
print(list(reversed(lista)))
print(tuple(reversed(lista)))
print(set(reversed(lista))) # em conjuntos não definimos a ordem dos elementos

#podemos interar sobre o reversed
for letra in ("rebecca mariah"):
    print(letra, end="")

#podemos fazer o mesmo sem usar o for
print("".join(list(reversed("rebecca maraiha"))))

#Já vimos com fazer com o slice
print("rebecca mariah"[::-1])

#podemos tbm utilizar o reversed em loops
for n in reversed(range(0,10)):
    print(n)

# Apesar que tambem vimos como fazer isso no range
for n in range(9, -1, -1):
    print(n)