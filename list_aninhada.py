"""
Em algumas linguagens de prograação possuem uma estrutura de dados chamadas de arrays,
que podem ser uni dimensionais ( arrays ou vetores), ou multidimensionais(matrizes)

"""
# Exemplo
lista = [[1,2,3],[4,5,6],[7,8,9]] # matris 3x3
print(lista)
#Como acessar dados
print(lista[0][1]) # linha[0] coluna[2]
print(lista[2][0])

# Como interar com loops
for listas in lista: # modo tradicional de loops
    for numero in listas:
        print(numero)

#list comprehensions
[[print(valor) for valor in listas] for listas in lista]

# outro exemplo:

#Gerando um tabuleiro ou matriz 3x3
tabuleiro = [[numero for numero in range(1,4)] for valor in range(1,4)]
#primeiro for criou as linhas o segundo as colunas
print(tabuleiro)

#Gerando jogada para o jogo da velha
velha = [["x" if numero % 2 == 0 else "o" for numero in range(1,4)]for valor in range(1,4)]
print(velha)

# Demontracao de valores iniciais
print([["&" for i in range(1,4)]for j in range(1,4)])