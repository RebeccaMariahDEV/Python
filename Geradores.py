"""
Geradores:

- Geradores (Gnerators) são  Interadores (Interators):

OBS: O contrario não é verdadeiro, ou seja , nem todo iterator é um generator

Outras informaçoes, generators apode ser criados com funções geradorasa, funções geradoras utilizam yield,
Generators podem ser criados com funções geradores.

Diferençã entres funções e geradores  de funções

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

/Functions                                     /Generator functions
utiliza return                                   utilizam yield
retorna uma vez                                  pode utilizar yield varias vezes
quando execultada retorna um valor|               quando execultada retorna um generator

# OBS: uma generator function não é um generator ela gera um generator

gen = cont(8)
print(type(gen)) #<class 'generator'>
print(next(gen))
# ate dar erro StopInte.....

# Utilizando a função em um for
for n in gen:
    print(n)


"""

# exemplo de Generator function
def cont(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador # contagem de 1 em 1, ele não sai ou termina a função
        contador += 1

gen = cont(10)
print(next(gen))
print("\n")

for n in gen:
    print(n)

# ou gerando ele em uma lista

