"""
Conjuntos

    - conjuntos: em qualquer linguagem de programação, estamos fazendo referencia:
    teoria de conjuntos da Matematica.

Em python os conjuntos são chamados de sets:
Como na matematica Sets nao possuem valores duplicados,
Sets nao possuem valoresm ordenados
Elementos não sao acessados via indice, ou seja, nao sao indexados:

Conjuntos são bons para utilizardos quando precisamos armazenar elementos
mas nao nos importamos com a ordem deles. Quando nao precisamos se preocupar
com chaves, valores e itens duplicados.

Os conjuntos (Sets) sao representados por {}

Diferença entre conjuntos (Sets) e mapas (dict)
    - Um dict tem chaves e valor,
    - Um conjunto te apenas valor

# Definindo conjuntos

#Forma 1
s = set({1, 2, 5, 5, 7, 8, 3, 1, 2, }) #Repare que temos valores repetidos
print(type(s))
print(s)
# OBS: ao criar um conjunto, caso seja adicionado um valor existente, o mesmo
#nao gera erros e nao fara parte do conjunto

s = {1, 3, 4, 5, 6, 3, 2, 1, 4, } # Criação mais comum
print(s)
print(type(s))
# Oq vimos em outros elementos podemos usar em sets

# Verificando elementos em Sets
if 3 in s:
    print("tem")
else:
    print("nao")

# Importante lembrar que alem de nao conter valor dulicado, nao tem ordem


lista = [25, 99, 3, -1, 6, 78, 1000, 25, 3]
print(f'{lista} com {len(lista)} elementos')
print(len(lista))
# Lista aceta valores duplicados
tupla = (25, 99, 3, -1, 6, 78, 1000, 25, 3)
print(f'{tupla} com {len(tupla)} elementos')
print(len(tupla))
#Tupla aceita valores duplicadas
dicionario = {}.fromkeys ([25, 99, 3, -1, 6, 78, 1000, 25, 3], "dict")
print(f'{dicionario} com {len(dicionario)} elementos')
print(len(dicionario))
# Dicionario nao aceita chaves duplicadas

Set = {25, 99, 3, -1, 6, 78, 1000, 25, 3}
print(f'{Set} com {len(Set)} elementos')
print(len(Set))
# Conjuntos nao aceitam valores duplicados
# Em set ele nao gera um ordem, ele modifica e coloca na ordem q ele quer

# Podemos misturar dados em sets
s = {1, "b", True, 22.67, -6}
print(s)
# Podemos interar valores em um set
for valor in s:
    print(valor)

# Uso interessantes com set
# Imagine que fizemos um formulario de cadastro de visitantes
#Os visitantes informam a cidade de onde vieram
# Adicionamos cada cidade em uma lista, já q em listas pode ter repetições

cidades = ["belo horizonte", " sao paulo", "campo grande", "cuiaba", "cuiaba", " sao paulo", "belo horizonte"]
print(len(cidades))

# Agora precisamos saber quantas cidades distintas temos
# Como resolver??!
print(len(set(cidades)))

# Adicionando elementos em um conjunto
s = {1, 2, 3, 4}
s.add(5)
s.add(5) # Duplicidade nao gera erro porem ele é ignorado
print(s)
# Conjuntos sao mutaveis

# Remover elementos em um conjunto
c
print(s)
#Forma 1
s.remove(3) # nao é indice, isso é o valor que quero remover
print(s)
# OBS: caso nao tenha o valor dara erro keyErro

# Forma 2
s.discard(2) # OBS: se o valor nao existir, nenhum erro é gerado(nessa forma)
print(s)
# Nenhum valor é retornavel

# Copiando um conjunto para outro
# Forma 1 deep copy
novo = s.copy()
# No deep copy se cria dois elementos separados
print(novo)
print(s)
novo.add(5)
print(novo)
print(s)
# Forma 2 Shellow copy
novo = s
novo.add(5)
print(novo)
print(s)

#Limpando o set

s = {1, 2, 3, 4}
s.clear()
print(s)

#metodos matematicos

#Imagine que temos dois conjuntos : um contendo estudantes de Python, outro de Java
estudantes_python = {"Matheus", "Aline", "Renata", "Bruno", "Gabriela"}
estudantes_java = {"Erick", "Gabriela", "Nathasha", "Romilda", "Hermione", "Renata"}

#Veja q alguns alunos estudam Python e Java

# - Precisamos gerar um conjunto unico com os nomes dos estudantes
# # Forma 1 union
# unicos = estudantes_java.union(estudantes_python)
# print(unicos)
# # Obs: nao repeti nome
#
# #Forma 2 Utilizando o pipe|
# unicos2 = estudantes_python | estudantes_java
# print(unicos2)
#
# # Em Sets não pode somar para juntar um com o outro

#Gerar um conjunto q esta nos dois cursos
# Forma 1
ambos = estudantes_java.intersection(estudantes_python)
print(ambos)
#Forma 2, utilizando o & comercial
ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Conjunto de estudantes de um grupo so
so_python = estudantes_python.difference(estudantes_java)
print(so_python)
# Esse metodo compara todos os nomes e retorna o restante deles q nao sao duplicados
so_java = estudantes_java.difference(estudantes_python)
print(so_java)


# Lembrete importante
#Soma, max, min, len
# Isso so acontece se os valores forem inteiros e reais

s = {1, 3, 4, 6, 8, 99, 78}
print(len(s))
print(min(s))
print(max(s))
print(sum(s))

"""
