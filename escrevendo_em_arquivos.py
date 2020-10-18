"""
Escrevendo em arquivos

Para esquecer um arquivos precisamos abrir igual fazemos para ler, porem em outro formato.

Aberto para leitura, só podemos ler
Aberto para escrita, só podemos escrever

Ao abrir um arquivo para escrita o arquivo é criado no sistema

Abrindo um arquivo para escrita com o modo w, podemos modificar ele
Se ele não existir ele será criado
"""
# exemplo de escrita - modo "w" ou write (escrever)
with open("novo.txt", "w") as arquivo:
    arquivo.write("escrever dados em um arquivo assim é mais facil\n")
    arquivo.write("podendo ter varias linhas que quiser\n")
    arquivo.write("novos dados\n")
    arquivo.write("dados modificados\n")

#OBS: para escrevermos dados em um arquivo, apos abri-lo utilizamos a func write()
# essa func recebe uma str como parametro, se não dara TypeError

# forma tradicional de abrir um arquivo

arquivo = open("texto.txt", "w")
arquivo.write("Dá para acrescentar teste em algo ja existente\n")
arquivo.closed

