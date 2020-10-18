"""
Sorted
OBS: não confunda com a func sort() que já estudamos em listas, o sort só funciona em listas.
Podemos utilizar o sorted() com qualquer interavel.
Como o nome diz, serve para ordenar.

O sorted modifica e cria uma nova lisra
Não importa sé  é uma tupla, ele sempre retorna uma lista

# Exemplo
numeros = 6, 1, 8, 2
print(sorted(numeros)) # ordena do menor ao maior
print(numeros)


"""
# numeros = [6, 1, 8, 2]
# # Adicionando parametros ao sorted()
# print(sorted(numeros, reverse=True)) # Maior para o menor
# print(sorted(numeros)) # menor para o maior
# print(tuple(sorted(numeros, reverse=True))) #Convertendo em tupla
#
# # Para coisas mais complexas
# usuarios = [
#     {"username": "rebecca", "twets":["fã de pizza", "me sinto o rafael das tn"]},
# {"username": "marcel", "twets":["fã de pizza", "me sinto o rafael das tn", "odeio segundas"]},
# {"username": "bruna", "twets":[]},
# {"username": "lucca", "twets":["fã de pizza", "me sinto o rafael das tn", "adoro bolos"], "cor": "azul", "musica": "rock"},
# {"username": "hilary", "twets":["fã de pizza"]},
# {"username": "gal", "twets":[], "cor": "preto"}
# ]
#
# print(usuarios)
# print(sorted(usuarios, key=lambda usuario: usuario["username"], reverse=False)) # ordem alfabetica
# print(sorted(usuarios, key=lambda usuario: usuario["username"], reverse=True)) #ordem de criação
#
# # Ordem por twets
# print(sorted(usuarios, key=lambda usuario: len(usuario["username"])))

# Ultimo exemplo
musicas = [
    {"titulo": "me gusta", "tocou": 5},
    {"titulo": "candy man", "tocou": 2},
    {"titulo": "saudade", "tocou": 7},
    {"titulo": "sinonimo", "tocou": 9},
    {"titulo": "cry", "tocou": 3},
 ]
# Menos tocada
print(sorted(musicas, key=lambda musica: musica["tocou"]))
# Mais tocada
print(sorted(musicas, key=lambda musica: musica["tocou"], reverse=True))