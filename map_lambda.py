"""
Map
( map não é o mesmo que dict, aqui fazemos função valor)
Com map fazemos mapeamento de valores para função

import math
def area(r):
    Calcula a area de um cirgulo com raio r
    return math.pi * (r **2)
print(area(2))
print(area(5.3))

raios = [2, 5, 7, 13, 0.4, 7, 8]

# forma comum
areas = []
for r in raios:
    areas.append((area(r)))
print(areas)

#Foma 2 - map
areas = map(area, raios) # map é uma funcao que recebe dois valores, primeiro func depois interavel
print(list(areas))
print(type(areas))
# Aq retorna um map object, podemos transformar em list, tuple etc

# forma 3 map com lambda
print(list(map(lambda r: math.pi * (r ** 2), raios)))
# Obs: apos utilizar a função map() depois da primeira utilização do resultado, ele zera

Para fixar
Temos dados interaveis:
dado: a1, a2...
temos função:
função: f(X)
Utilizamos a função map(f, dados) onde map ira mapear cada elemento dos dados e aplicar a funcao
Map object: f(a1), f(a2)...


"""
# Outro exemplo
cidades= [("berlin", 29), ("Cairo", 36),("Sao Paulo", 25), ("Tokio", 15), ("Dubai", 39)]
print(cidades)

# f = 9/5 * c + 32
#lambda
c_para_f = lambda dado: (dado[0], (9/5) * dado[1] +32)
print(list(map(c_para_f, cidades)))
