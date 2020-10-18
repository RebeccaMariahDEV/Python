"""
Funções com retornos

numeros =[ 1, 2, 3]
ret_pop = numeros.pop()
print(f"retorno de pop: {ret_pop}")
ret_pr = print(numeros)
print(f"retorno do print: {ret_pr}")

#OBS: Em Python quando uma função nao retorna nenhum valor, o retorno é none

def quadrado_de_7():
    print(7 * 7)# aqui não tem retorno nenhum

ret = quadrado_de_7()# essa função nao retorna nada, ela só imprime

print(f"retorno: {ret}")

OBS: Funções que retornam esses valores é com a palavra return
- Não precisa nescessariamente criar uma variavel para receber o retorno de uma funcao,
podemos passar a execucao da funcao para outras funcoes ou mesmo para o print

# Vamos refatorar essa função par q retorne um valor
def quadrado_de_7():
    return 7 * 7

ret = quadrado_de_7()# essa função nao retorna nada, ela só imprime

print(f"retorno: {ret}")# ret variavel para o retorno
print(f"retorno: {quadrado_de_7() + 1}")

# refatorando a 1 função
def diz_oi():
    return "oi " # nesse caso precisa do print lá em baixo para executar

alguem = "pedro"

print(f"retorno: {diz_oi() + alguem}")
#OBS: O return ajuda caso você queira acrescentar algo a mais depois ou aproveitar o dado para outras coisas

OBS: sobre a palavra reservada return:
- Ela finaliza a função, ou seja, ela sai da execução da função
- Podemos ter em uma função diferentes returns
- Podemos em uma função retornar qualquer tipo de dados e ate multiplos valores

# Exemplo 1 - Ela finaliza a função, ou seja, ela sai da execução da função
def diz_oi():
    print("Antes do retorno")
    return "Oi"
    print("Estou sendo execultado apos o retorno")
    #Apos o retorna nada mais é execultado

print(diz_oi())

#Exemplo 2 - Podemos ter em uma função diferentes returns
def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    else:
        return "b"

print(nova_funcao())

# exemplo 3 - Podemos em uma função retornar qualquer tipo de dados e ate multiplos valores

def outra_funçao():
    return 2, 3, 4, 5

num1, num2, num3, num4 = outra_funçao() # não precisa guardar afunção em outra variavel

print(num1, num2, num3, num4) # porem aq estamos desempacotando a função que retorna uma tupla
print(outra_funçao())


"""
# Criar uma funcao para jogar uma moeda

from random import random

def jogar_moeda():
    # Gera um numero pseudo randomico entre 0 e 1
    if random() > 0.5:
        return "cara"
    return "coroa"

print(jogar_moeda())

# Essa funçao randomica ela é pseudo aleatorio, ou seja ela é mais ou menos aleatorio, pode gerar repetições

#Erros comuns da utilização do return, que na verdade nem é um erro, porem é codificação desnecessaria

def e_impor():
    numero = 5
    if numero % 2 != 0:
        return True
    else:# se só temos duas opcoes nao precisa do else, e o return fica na linha do if
        return False

print(e_impor())