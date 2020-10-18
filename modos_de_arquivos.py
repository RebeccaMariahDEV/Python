"""
Modos de abertura em arquivos

"r" -> abre para leitura de arquivos
"w" -> abre para escrita de arquivos - sobrescreve caso o arquivo já exista

Em docs do python tem outros
"x" -> abre para escrita, somente se o arquivo não existir, caso contrario dara falha FileExistsError
"a" -> abre para escrita adicionando o conteudo ao final do aquivoi
    Obs: abrindo no modo "a' se não existir sera criado, se existir sera adicionado ao final
"+" -> abre um arquivo para atualização, abre em leitura e em escrita, porem junto ao  modo que você queira
"""
# Exemplo x
#with open("lista.txt", "x") as arquivo:
#    arquivo.write("teste de conteudo\n")

# exemplo a
with open("texto.txt", "a") as arquivo:
    arquivo.write(" teste de adicionar dados ao arquivo\n")
    arquivo.write("esse arquivo já foi rescrito e modificado\n")

with open("texto.txt", "a+") as arquivo:
    arquivo.write(" teste de adicionar dados ao arquivo\n")
    arquivo.write("esse arquivo já foi rescrito e modificado\n")