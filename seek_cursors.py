"""
Seek e Cursor

A função Seek é utilizada para movimentar o cursor pelo arquivo

"""

arquivo = open("texto.txt")
# print(arquivo.read())

# movimentando o cursor pelo arquivo, com a função seek
arquivo.seek(0)
"""
A função seek() é utilizada para movimentação do cursor pelo arquivo, 
ela recebe um parametro q indica onde queremo colocar o cursor

"""
# print(arquivo.read())
# arquivo.seek(24)
# print(arquivo.read())

"""
Função para ler linha a linha
readline()
Ou linhas
readlines()
"""
res = arquivo.readline()

print(type(res))

print(res)

print(res.split(' '))

# print(arquivo.readlines(3))
linhas = arquivo.readlines()
print(len(linhas))

"""
OBS: quando abrimos um arquivo com a função open() é criado uma conecção entre o computador e o programa
essa conecção é chamada de streaming
ao finalizar os trabalhos, devemos fechar essa conecção, para isso utilixamos o close()

Passos para se trabalhor com um arquivo
1 abrir:
arquivo = aopen(nome do arquivi)

2 trabalhar o arquivo
print(nome.read())

3 fechar o arquivo
nome.close()

Com a função read() podemos limitar quantos caracteres poderão ser lidos do arquivo.

"""
print(arquivo.closed)# verifica se esta aberto ou fechado
arquivo.close()
print(arquivo.closed)
# quando fechado ele retorna true

#OBS se tentar manipular o arquivo fechado dara ValueError