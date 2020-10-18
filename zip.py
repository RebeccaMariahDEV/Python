"""
Zip

Ele cria um interavel(chamado zip object)que agrega elemento de cada um dos interaveis passados como entrada em pares.
#Exemplo
lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9]
zip1 = zip(lista1, lista2)
print(zip1) #zip object
#Sempre podemos gerar uma lista, tupla, ou dict
Para cada interavel do zip ele converte para tupla dividindo as listas por iguais.
A primeira vez utilizada ele some igual o filter
#OBS: o zip utiliza como parametro a menor lista de interaveis, entao ele para se outra lista for maior dq a primeira lista

# Exemplos

lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,10]
zip1 = zip(lista1, lista2, "abcde")
print(list(zip1))
print(set(zip1))
print(tuple(zip1))
zip1 = zip(lista1, lista2)
print(dict(zip1))
l1 = ["a ","b","c","d","e"]
l2 = [1,2,3,4,5]
z = zip(l1, l2)
print(dict(z))
lista3 = [12,13,14,15,16,17,18]
zip1 = zip(lista1, lista2, lista3)
print(list(zip1))

# Podemos usar diferentes tipos de interaveis com zip, lembrando q dict tem q usar .valeus no fim para pegar so os valores

# Exempos diferentes interaveis:
tupla = (1,2,3,4,5)
lista = [1,2,3,4,5]
set = {1,2,3,4,5}
zt = zip(lista, tupla, set)
print(list(zt))
dados = [(0,1), (1,2), (2,3), (3,4), (4,5)]
print(list(zip(*dados)))


"""

prova1 = [89, 91, 78]
prova2 = [98, 89, 53]
alunos = [ "maria", "antonio", "daniella"]
final = {dado[0]:max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)} # aqui e um dict comprehension
print(final)

# Podemos utilizar o map
final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(final))