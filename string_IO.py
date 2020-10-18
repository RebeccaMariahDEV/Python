"""
StringIO:

ATENÇÃO: para ler ou escrever dados, o software precissa ter permição:
    - permição para ler -> leitura do arquivo
    - permição para escrever -> escrita de arquivo

Utilizado para ler e criar arquivos em memoria.


"""
# Para utilizar devemos fazer o import
from io import StringIO

mensagem = "Essa é uma string normal \n"

#Podemos criar um arquivo em memoria já com uma string inserida ou uma vazia para escrever depois
arquivo = StringIO(mensagem)
# arquivo = open("arquivo.txt", "w")

# Agora tendo o arquivo, podemos utilizar oque já sabemos de arquivos
print(arquivo.read())

# Escrever outro texto
arquivo.write("Quero terminar e aprender a programar logo ")

# Podemos inclusive movimentar o cursor
arquivo.seek(0)

print(arquivo.readlines())
