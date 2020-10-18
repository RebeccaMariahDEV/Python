"""
Erros comuns em Python

Atenção: é importante prestar atenção e aprender a ler as saidas de erros grandes pela execulção
do nosso codigo

Os mais comuns:
- SyntaxError -> ocorre quando o python encontra um erro de sintaxe. ou seja, você escreveu algo q
o python não reconheceu

# Exemplos:

a)
def funcao:
    print("oi")

b)
def = 1

c)
return
OBS: return tem que estar dentro de uma função ou ação

2 - Name error -> ocorre quando  uma variavel ou função não foi definida

# Exemplo

a)
print(oi)

b)
oi()

3- TypeError -> ocorre quando uma função/operação/ação é aplicado a um tipo errado

# Exemplo
a)
print(len(6))

b)
print("oi" + [])

4 - IndexError -> ocorre quando tentamos acesssar um elemento em uma lista ou outro tipo de dado indexado utilizando
um indice invalido

# Exemplo

a)
lista = ["Rebecca"]
print(lista[0])

b)
lista = ["Oi, tudo bem"]
print(lista[0][15])

c)
tupla = ("geek")
pint(tupla[0][10])

5 - ValueError -> ocorre quando uma função/operação buit-in (integrada) recebe um argumento do tipo correto
com valor inapropriado

a)
print(int("ola")) # dara o mesmo valor de erro

6 - KeyError-> ocorre quando tentamos acessar um dicionario com uma chave q não existe

a)
dic = {}
print(dic["ola"])
# dict vazio, lemre dicionario é chave:valor

7 AtibuteError -> Ocorre quando uma variavel não tem um atributo ou função

a)
tupla = (1,2,3,4,67,89,54,5,34)
print(tupla.sort)
sort é para uma lista

8 - IndentationError -> ocorre quando declaramos as funções de um bloco

a)
for n in range(10):
print(n)

Lembrando que temos outros tipos de erros, porem esses são os mais comuns

OBS: exceptions e erros são sinonimos

"""