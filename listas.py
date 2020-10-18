"""
# checando valosres dentro de uma lista
if "e" in lista3:
    print("encontei o e")
else:
    print("nao tem")

# podemos cordernar uma lista
lista.sort()
print(lista)

# numero de ocorrencias de valor em uma lista

print(lista.count(3))
print(lista5.count("e"))

# add elementos em lista
# utilizamos a funcao append

lista.append(2512)
print(lista)
lista.append([10, 23, 30, 17])
print(lista)


# pode ter lista dentro de outras listas

# podemos extender uma lista
lista.extend([ 34, 56, 78, 90, 93, 123 ])
print(lista)
lista.sort()
print(lista)

#podemos adicionar valores nas possicoes que quisermos ex:
lista.insert(4, 4)
sempre utilizando o .insert()

# fundindo uma lista na outra
pode ser:
lista6 = lista + lista5
ou
lista += lista5

#reverse de lista
lista.reverse()
lista5.reverse()

podemos utilizar a lista mais o [: : -1]
print(lista[::-1], lista5[::-1])

#copiando lista
lista2.copy()
print(lista2)

#contando quantos elementos tem em uma lista
print(len(lista4))

#removendo o ultimo elementos de uma lista
lista.pop()
print(lista)
# OBS: se quiser saber o ultimo elemento é so utilizar o ex: lista.pop para retornar o valor
podendo tambem remover o valor do indice que quiser atraves do (x)
# si nao houver elemento no indice informado teremos erro de syntaxe

#para limpar a lista
lista5.clear
print(lista5)
ela aparecera vazia

#repetindo elementos em uma lista
print(lista * 3)

#transformando str em lista
mozi = "Marcelo mussi"
mozi = mozi.split()
print(mozi)
#obs por padrao o split separa os elementos da lista por espaco

exemplo 2
mozi = "rebecca,mussi,cacau"
mozi = mozi.split(",")
print(mozi)

#uma lista em str
mozi = " ".join(lista6)
print(mozi)
#pega a lista6 e coloca espaço entre cada elemento e transforma em str
#pode ser montada usando o separador por qualquer ouro caracter q vc quiser

#interando sobre lista
utilizando for
soma = 0
for elemento in lista4:
    soma = soma + elemento
    print(soma)

utilizando While
carrinho = []
produto = ""

while produto != "sair":
    print("adicione um produto: ")
    produto = input()
    if produto != "sair":
        carrinho.append(produto)
for produto in carrinho:
    print(produto)

cores = ["azul", "amarelo", "verde", "vermelho", "roxo", "branco"]
for cor in cores:
    print(cor)
indice = 0
while indice< len(cores):
    print(cores)
    indice += 1

#criando indice com for
for indice, cor in enumerate(cores):
    print(indice, cor)

#encontrar indice de um elemento
numeros = [5, 6, 7, 8, 9, 10, 11, 12]
print(numeros.index(6))

#busca dentro de um range
print(numeros.index(5, 1)) paratir do indice(1) ou vc escolhe qual quer
print(numeros.index(8, 3, 8)) # para procurar entre o 3 e o 8

#para uma lista com slince
print(lista[1::]) # [inicio: fim: passo]
print(lista[: : 2]) # [inicio: fim: passo]

#valores
print(sum(lista))#soma
print(max(lista))# maximo valor
print(min(lista))#minimo valor
print(len(lista)) #tamanho da lista

#transforamando lista em tupla
tupla = tuple(lista)
print(tupla)

#Desempacotamento de lista
lista = [1, 99, 156]
num1, num2, num3 = lista
print(num1)
print(num2)
print(num3)
# se tiver mais elementos para desempacotar tera que aumentar as variaveis ou diminuir a lista

#copiando uma lista para outra (Shallow)
lista = [1, 2, 3]
nova = lista.copy()
nova.append(4)
print(nova)
#quando utilizamos lista.copy copiamos as lista porem se acrescentar algo a mais a outra lista nao vai alterar o valor
da anterior
#porem podemos alterar as listas por atribuiçao
# apos realizar a modificacao em uma das lista, ambas se modificam (chamado de Shallow copy)

"""


lista2 = ["r", "e", "b", "e", "c", "c", "a"]
lista3 = []
lista4 = list(range(11))
lista5 = list("Rebecca")
lista6 = ["rebecca", "marcelo", "cacau"]

cores = ["azul", "amarelo", "verde", "vermelho", "roxo", "branco"]
numeros = [5, 6, 7, 5, 8, 9, 10, 11, 12]

