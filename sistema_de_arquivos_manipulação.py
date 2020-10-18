"""
Sistema de Arquivos - Manipulação


"""
import os
# descobrindo se o arquivo ou diretorio existe
print(os.path.exists("arquivo.txt")) # retorna true or false
print(os.path.exists("novo.txt")) # nesse caso é verdadeiro

# Diretorio
print(os.path.exists("default_dict.py")) # as verificações são feitas aqui dentro da pasta de aulas, são relativos

# Path absolutos
print(os.path.exists("//becca//dev"))
print(os.path.exists("//users"))
# ainda não entendi como usar

"""
# Criando um arquivo
open("arquivo_teste.txt", "w").close()
 podendo passar o "a" ou outras coisa que aprendemos em como criar arquivos
 podemos utilizar o with para abrir tbm utilizando o as para dar um apelido e  pass para para (não farei nada)
 
 
"""
# melhor furma de se criar

os.mkdir("arquivo_test.txt")
"""
OBS: se o arquivo já existir dara erro FileExistError
No mac talves não funcione, pois dara erro.

Os diretorios serão criados a onde estara sendo executado
     - O diretorio será criado com o uso do mkdir
     
"""


