"""
Min e Max

Max -> retorna o maior valor de um interavel ou maior de dois ou mais elementos

# Exemplos
lista = [1, 6, 67, 89, 456, 34, 2, 12]
tupla = (1, 6, 67, 89, 456, 34, 2, 12)
set = {1, 6, 67, 89, 456, 34, 2, 12}
dicionario = {"a":1, "b":6, "c":67, "d":89, "e":456, "f":34, "g":2, "h":12}
print(max(lista))
print(max(tupla))
print(max(set))
print(max(dicionario))# Retorna a maior chave
print(max(dicionario.values())) #.values retorna o maior valor

# outro jeito de uzar o max
v1 = int(input("primeiro valor: "))
v2 = int(input("segundo valor: "))
print(max(v1, v2))
# Podemos passar str, float e int

Min -> retorna o menor valor de um interavel ou menor de um ou mais elementos

# Exemplos
lista = [1, 6, 67, 89, 456, 34, 2, 12]
tupla = (1, 6, 67, 89, 456, 34, 2, 12)
set = {1, 6, 67, 89, 456, 34, 2, 12}
dicionario = {"a":1, "b":6, "c":67, "d":89, "e":456, "f":34, "g":2, "h":12}
print(min(lista))
print(min(tupla))
print(min(set))
print(min(dicionario))
print(min(dicionario.values()))

# Exemplos mais complexos
nomes = ["ana", "maria", "luiz", "marcelo", "vanessa", "tim", "sandro"]
print(nomes)
print(max(nomes))
print(min(nomes))
# Aqui ele leva em conta a ordem alfabetica dos nomes
print(max(nomes, key=lambda nome: len(nome))) # maior nome
print(min(nomes, key=lambda nome: len(nome)))# menor nome


"""
musicas = [
    {"titulo": "me gusta", "tocou": 5},
    {"titulo": "candy man", "tocou": 2},
    {"titulo": "saudade", "tocou": 7},
    {"titulo": "sinonimo", "tocou": 9},
    {"titulo": "cry", "tocou": 3},
 ]
print(max(musicas, key=lambda musica: musica["tocou"]))
print(min(musicas, key=lambda musica: musica["tocou"]))
mais = max(musicas, key=lambda musica: musica["titulo"])
mais1 = max(musicas, key=lambda musica: musica["tocou"])
print(mais, mais1)
minimo = min(musicas, key=lambda musica: musica["tocou"])
minimo1= min(musicas, key=lambda musica:musica["titulo"])
print(minimo, minimo1)

# desafio, só o titulo
print(max(musicas, key=lambda musica: musica["tocou"])["titulo"])
print(min(musicas, key=lambda musica: musica["tocou"])["titulo"])

# sem usar mxa, min e lambda
max = 0
for musica in musicas:
    if musica["tocou"] > max:
        max = musica["tocou"]

for musica in musicas:
    if musica["tocou"] == max:
        print(musica["titulo"])

min = 90
for musica in musicas:
    if musica["tocou"] < min:
        min = musica["tocou"]

for musica in musicas:
    if musica["tocou"] == min:
        print(musica["titulo"])
