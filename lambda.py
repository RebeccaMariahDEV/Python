"""
Utilizando lambda

Oq são lambdas?!
São funções sem nome, ou seja funções anónimas

# Função em py

def qualquer(x):
    return 3 * x + 1

print(qualquer(7))
print(qualquer(5))

# Expressão lambda

lambda x: 3 * x + 1
# o x é o parametro e o retorno é o resto da função

# Como utilizar a expressao lambda
calc = lambda x: 3 * x + 1
print(calc(7))
print(calc(5))


"""
# Podemos ter expressoes lambdas em multiplas entradas
nome_completo = lambda nome, sobrenome: nome.strip().title() + " " + sobrenome.strip().title()

#A função do strip é retirar os espaços do inicio e fim de uma str

print(nome_completo(" REBECCA   ", "  MARIAH  "))
print(nome_completo("  MARCELO  ", "  MUSSi  "))

# Em funções py podemos ter nenhuma ou varias entradas, em lambda tbm
amar = lambda : "Como não me amar?!"
uma = lambda x: 3 * x + 1
duas = lambda x, y: (x * y) ** 0.5
tres = lambda x, y, z: 3 / (1 / x + 1/ y + 1 / z)
# n = lambda x1, x1 , ......: <espressao>
print(amar)
print(uma(6))
print(duas(6,8))
print(tres(3,6,8))
#OBS: se passar mais argumentos do que paraetros dara erro

autores = ["j. j. lupin", "Ema whatson", "Montero Lobato", "Enrique Martin", "j. j. tolken", "Clarisse Lispector",
           "dom casmuro", "camila alves"]
print(autores)
autores.sort(key= lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)# nao da para criar o lambda direto no print
"""
 Função quadratica
 f(x) = a * x **2 + b * x + c
"""
# Definindo a função
def gerador_quadratico(a, b, c):
    """ retorna a função  f(x) = a * x **2 + b * x + c """
    return lambda x: a * x ** 2 + b * x + c
teste = gerador_quadratico(2,3,-5)
print(teste(0))
print(gerador_quadratico(3,5,-5)(2))
print(teste(1))
print(teste(2))

"""
Geralmente as funções lamdas são usadas para filtragem e ordenação de dados,
porem elas não se limitam a isso
"""