"""
Leitura de Arquivos

Para ler o conteudo de um arquivo, utilizamos a função integrada open()
Que literalmente significa abrir

Sobre open():
    - Na forma mais simples de utilizar nós passamos apenas um parametro de entrada,
    que neste caso é o nome do arquivo as ser lido, essa função retorna um _io.TextIOWrapper,
    é com ele que trabalhamos então.

Por padrão a função open abre o arquivo para leitura, esse arquivo deve existir, se não dara erro

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>

name='texto.txt = nome do arquivo
mode='r' = mode de leitura
encoding='cp1252' = caracteres especiais

"""

arquivo = open("texto.txt")

print(arquivo)
print(type(arquivo))

ret = arquivo.read()
print(type(ret))
print(ret)

# para ler o conteudo de um arquivo apos da abertura, devemos utilizar a função read()

# print(arquivo.read())

# print(arquivo.read()) OBS: em Python ele utiliza um recurso para trabalhar com arquivos chamado cursor,
# esse cursor funciona como o cursor quando estamos escrevendo

# A função read() le todo o conteudo do arquivo
