"""
# dicionarios e como utilizalos

# obs: em algumas linguagens de programações sao conhecidos por mapas
isso pq dicionarios sao coleçoes de tipo chaves/valor.

dicionario sao repesentados por chaves

OBS: Sobre dicionarios
    - Chave e valor sao separados por (:) ex: "chave:valor"
    - Tanto chaves quanto valor pode ser de qualquer tipo de dados
    - Podemos misturar tipos de dados:

# Criação de dict
# Forma mais comum de dict
pais = {"Br": "Brasil", "EUA": "Estados Unidos", "Ln": "Londres"}

print(pais)
print(type(pais))

# Forma menos comum
pais = dict(br="Brasil", eua="Estados Unidos", py="Paraguai")
print(pais)
print(type(pais))

# Acessando elementos

# Forma 1: acessando via chaves, da mesma forma q via tupla
print(pais["Br"])
# obs: caso tentamos fazer um acesso utilizando uma chave inexistente
#teremos um erro key erro

# Forma 2: Recomendado, usando get
print(pais.get("Br"))
print(pais.get("ru"))

pais = {"Br": "Brasil", "EUA": "Estados Unidos", "Ln": "Londres"}
pais = pais.get("Ln")

# Caso o get nao encontre a chave informada, sera retornado o valor None

if pais:
    print(f"Encontrei o pais {pais} ")
else:
    print("Não encontrei")

#Tambem pode ser feito assim:
pais = {"Br": "Brasil", "EUA": "Estados Unidos", "Ln": "Londres"}
pais = pais.get("Ln", "Não encontrei o pais")
print(f"Encontrei o pais {pais} ")

# Podemos definir um valor padrão para caso não encontrarmos o objeto com a chave informada

pais = {"Br": "Brasil", "EUA": "Estados Unidos", "Ln": "Londres"}

# Podemos verificar se uma determinada chave esta em um dict

print("Br" in pais)
print("EUA" in pais)
print("ru" in pais)
print("Londres" in pais)

if "ru" in pais:
    russia = pais["ru"]

#Podemos verificar se determinada chave esta no dict ou nao

pais = {"Br": "Brasil", "EUA": "Estados Unidos", "Ln": "Londres"}
pais = pais.get("Ln", "Não encontrei o pais")
print(f"Encontrei o pais {pais} ")

# Tuplas, por exemplo , são bastantes interessantes como chaves de dict,
pois elas sao imutaveis
locais = {
    (45.678, 34.890): "Clube pinheiros",
    (57.890, 24.654): "Casa",
}
print(locais)

# Adicionar elementos em um dict
receita = {"janeiro": 2.500, "fevereiro": 2.400, "março": 2.400, "abril": 1.800}
print(receita)
# Forma 1 = Mais comum
receita["maio"]= 1800
print(receita)

# Forma 2
novo_dado = {"junho": 1.500}
receita.update(novo_dado) # poderia fazer: receita.update({chave:valor})

print(receita)

#atualizando dados no dict

#forma 1

receita["maio"] = 1.500
print(receita)

# Forma 2
receita.update({"maio": 1.400})
print(receita)

# Conclusão:
# 1 A forma de addicionar novos elementos ou atualizar dados em um dict é a mesma,
# 2 em dict nao podemos ter chaves repetidas.

# Remover dados

receita = {"janeiro": 2.500, "fevereiro": 2.400, "março": 2.400, "abril": 1.800}
print(receita)

# Forma 1: Mais comum
ret = receita.pop("março")
print(ret)
print(receita)
# OBS:
# 1 Aqui precisa SEMPRE informar a chave exata, caso nao dara erro
# 2 Ao removermos um objeto, o seu valor é sempre retornado

# Forma 2
del receita["fevereiro"]
print(receita)
# OBS: nesse caso o valor removido nao é retornvel


"""
# Imagine que vc tenha um site de eletronicos, onde tem um carrinho de compras
"""
carrinh:
    prodito 1
        nome, quantidade e preço
    produto 2
        nome, quantidade e preço
        
# poderiamos criar uma lista para isso ?!
carrinho = []
produto1 = ["ps 4", 1, 1.800]
produto2 = ["GoW", 1, 150]
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)
# Teriaamos que saber qual o indece de cada informação no produto
# 2 usando tuplas
produto1 = ("ps4", 1, 1800)
produto2 = (" GOW", 1, 150)
carrinho = (produto1, produto2)
print(carrinho)

# 3 podemos usar o dict
carrinho = []
produto1 = {"nome": "ps4", "quantidade": 1, "valor": 1800}
produto2 = {"nome": "GOW", "quantidade": 1, "valor": 150}
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

#OBS:  dessa forma sabermos o nome e a quantidade do produto por chaves
# utilizando indice correto e exato
# ais facil de se localizar e melhor compriendido

# metodos para dict
'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

d = dict(a=1, b=2, c=3)
print(d)
d.clear() #utiliza para limpar dicionarios
print(d)

d = dict(a=1, b=2, c=3)
print(d)

# copy
novo = d.copy()
novo[ "d" ] = 4
print(d)
print(novo)

d = dict(a=1, b=2, c=3)
print(d)

# Foma 2: shallow copy
novo = d
print(novo)
novo["d"]=4
print(d)
# Isso vai funcionar em python em qualquer sentido

OBS: é um banco relacional é um local de dados nominados, um dict é um banco de dados relacionado,
onde tem chave e valor

"""
outro = {}.fromkeys("a", "b")
print(outro)
usuario = {}.fromkeys(["Nome", "idade", "email", "perfil"], "desconhecido")
print(usuario)
# OBS: o metodo fromkeys recebe dois parametros = um interavel e um valor
# ele vais gerar para cada valor do interavel uma chave e ira atribuir um valor a essa chave

veja = {}.fromkeys("teste", "valor") # Para cada letra ele interou o valor em cada chave
print(veja)

veja1 = {}.fromkeys(range(1,11), "novo")
print(veja1)


