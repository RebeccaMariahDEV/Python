"""
Debugando com PDB

PDB -> Python bug

# OBS: a utilização do print() para degugar codigo é uma pratica ruim

def dividir(a, b):
    print(f"a ={a}, b = {b}")
    try:
        return  int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f"Ocorreu um problema {err}"

print(dividir(5,8))

# Existem formas mais profisionais de se fazer o debug
# em python podemos fazer isso em diferentes ides

# Exemplo pycharm
def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f"Ocorreu um problema {err}"

print(dividir(8,0))

# Exemplo com pdb
#para utilizar o python deguber, precisamos importar a biblioteca pdb, e utilizar a função set_trace()

# comandos basicos do pdb
# l = listar onde estamos no codigo
# n = proxima linha
# p = imprime variavel
# c = continua e execução

import pdb

nome = "antonio"
sobrenome = "alves"
pdb.set_trace()
nome_complrto = nome + " " + sobrenome
curso = "python"
final = nome_complrto + " faz o curso de " + curso
print(final)

# exemplo 2

nome = "antonio"
sobrenome = "alves"
import pdb; pdb.set_trace()
nome_complrto = nome + " " + sobrenome
curso = "python"
final = nome_complrto + " faz o curso de " + curso
print(final)

# o debug é utilizado durante a criação do programa
# costumamos realizar todos os importes no inicio do arquivo
# por isso esse tipo de importe é utilizado somente onde vc quer debugar, depois é só apagar


# A partir do python 3.7 não é mais nescessario importar o pdb, pois ele foi incorporado como função
# chamada breakpoint()

# exemplo 3

nome = "antonio"
sobrenome = "alves"
breakpoint()
nome_completo = nome + " " + sobrenome
curso = "python"
final = nome_complrto + " faz o curso de " + curso
print(final)


"""
#OBS: cuidado com os comandos do degubr e variaveis

def somar(l, n, p, c):
    breakpoint()
    return l + n + p + c

print(somar(8,9,6,5))

#para mostrar variaveis tem q utilizar o p + a variavel
