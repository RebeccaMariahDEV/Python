"""
Teste de Memoria com Generators

# Sequencia de Fibinacci
1, 1, 2, 3, 5, 8, 13
1 + 1 = 2, 2+ 1 = 3, 3 + 2 = 5 .....


"""
def gerador(max):
    num = []
    a, b = 0, 1
    while len(num) < max:
        num.append(b)
        a, b = b, a + b
    return num
# # Teste
# for n in gerador(100):
#     print(n)

# geradores
def fib(max):# mais eficiente
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador += 1
# teste 2 geradores
for n in fib(100):
    print(n)

# Geradores são extremamente mais eficiente para o consumo de memoria