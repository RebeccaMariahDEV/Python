"""
Sistema de arquivos e navegação

No seu proprio computador tem dados slvos em arquivos, podendo ser eles videos, planilhas, fotos etc.

Os arquivos são associados a  sua extenção por exemplo arquivo.pdf, ele sera em pdf

OS arquivos são salvos em directory, que são pastas
Dentro do directory  tem sub directory em ordem hierarquica.
Conhecido como Arvore de directory, o principal é chamado de raiz ou Root

Para fazer uso de manipulação de arquivos do sistema, precisamos importar e fazer uso do modulo OS
OS -> Operating system

"""
# fazer import
import os

# getcwd() -> pega o  current work directory
print(os.getcwd())
# Retorna o path (caminho absoluto)

# Para mudar o directory , podemos utilizar o chdir()
# os.chdir("..")
# print(os.getcwd())

"""
A cada ves que é execultado o:
os.chdir("..")
print(os.getcwd())
Ele volta uma pasta, onde você estava ate chegar na raiz

print(os.path.isabs("aulas_de_python")) # retorna false ou true, forma para mac e linux

# OBS: Windows:
# Se você , infelismente( no caso eu), utiliza windows
# Tera que ter cuidado ao verificar um diretorio

# Forma para windows
print(os.path.isabs("C:\\users\\becca\\Dev")) # Agora deu True

print(os.name)

"""
#Podemos ter mais detalhes do sistema
# print(os.uname()) para mac/linux

# windows
# import sys
# print(sys.platform)

# print(os.getcwd())
#  var = os.path.join(os.getcwd(), "aulas_de_python")
#  os.chdir(var)
# print(os.getcwd())

# ainda não entendi como fazer em windows

#podemos listar os diretorios com o listdir
# print(os.listdir())

"""
Podemos utilizar o len() para verificar quantos arquivos tem aq
ou
quantos tem no computador inteiro

Podemos ter mais detalhes tbm com o scandir

"""
scan = os.scandir()
print(list(os.scandir()))
arquivos = list(os.scandir())
# print(os.listdir())
print(arquivos[0].name) # nome do arquivo
print(arquivos[0].inode()) # ??
print(arquivos[0].is_file()) # é um arquivo
print(arquivos[0].is_dir()) # é um diretorio
print(arquivos[0].is_symlink()) # é um link simbolico
print(arquivos[0].path) # caminho ate o arquivo
print(arquivos[0].stat()) # estatistica sobre o arquivo

# OBS: quando utilizamos a função scandir() precisamos fecha-la
scan.close()