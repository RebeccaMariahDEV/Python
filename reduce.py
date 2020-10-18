"""
Reduce

obs: A partir do python3+ a função reduce() não é mais uma função integrada (built-in). Agora temos
que importar e utilizar esta função a partir do modulo "functools'

Guido na Rossum: utilize a função reduce() se vc realmente precisar dela. Em todo caso,
99% das vezes um loop for é mais legivel.

Para entender o reduce

- imagine que voce tem uma colecao de dados

dados = [ a1, a2 ......]

E vc tem uma função que recebe dois parametros:

def funcao(y,z):
    return x * y

Assim como map e filter a func reduce recebe 2 parameros, funcao e interavel
recude( funcao, interavel )

A func reduce funciona da seguinte forma:
-passo 1: res1 = f(a1, a2) # aplica a funcao nos dois primeiros elementos da colecao e guarda o resultado
-passo 2: res2 = f(res1, a3)# aplica a funcao passando o resultado do passo 1 mais o 3 elemento e guarda o resultado,
e isso é repetido ate o final, ele sempre pega o resultado anterior
-passo 3: res3 = (res2, a4) e por ai vai

Em cada passo ela aplica a função passando  como pimeiro argumento o resultado da aplicação anterior. No final,
reduce() ira retornar o resultado final.

Alternativamente, poderiamos ver a função reduce() como:]
função(função(função(a1, a2), a3), a4), .....) , an)

"""
# Comofunciona na pratica?

# Vamos utilizar a função reduce para multiplicar todos os numeros de uma lista
from functools import reduce

dados = [2, 3, 23, 45, 345, 67, 897, 12, 34, 567]
# para utilizar o reduce precisamos de uma função q recebe 2 parametros

multi = lambda x, y: x * y
res = reduce(multi, dados) # reduce é utilizado como um for
print(res)

# Utilizando loops normal
res = 1
for n in dados:
    res = res * n
print(res)
