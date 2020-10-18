"""
Genereators Expression
Em aulas anteriores nós estudamos:
- list comprehensions
- dictionary comprehensions
- set comprehensions

Não vimos:
- Tuple comprehensions..... porque elas se chamam Generators

nomes = ["carlos" , "camila", "carla", "cassiano", "cristina", "vanessa"]

print(any([nome[0] == "c" for nome in nomes]))

OBS: O genereators oculpa menos memoria, por não criar uma lista, apenas um numero na memoria

#Poderiamos ter feito utilizando generators
nomes = ["carlos" , "camila", "carla", "cassiano", "cristina", "vanessa"]
print(any(nome[0] == "c" for nome in nomes)) #isso nao é um list comprehensions
#Assim como map e filter o resultado é apagado da memoria depois de usar

# retorna a quantidade de bytes em memoria do elemento passado como parametro

#Mostra quantos bytes a str ocupa em memoria, quanto maior a str mais espaço ocupa

print(getsizeof("Rebecca"))
print(getsizeof("Marcelo e cacau"))
print(getsizeof(9))
print(getsizeof(True))
"""
from sys import getsizeof

# Gerando uma lista de numeros com list comprehensions
list_comp = getsizeof([x * 10 for x in range(1000)])

# Set
set_comp = getsizeof({x * 10 for x in range(1000)})

#dict
dict_comp = getsizeof({x: x * 10 for x in range(1000)})

# Genereators
gen_comp = getsizeof(x * 10 for x in range(1000))

print(f'{list_comp}')
print(f'{set_comp}')
print(f'{dict_comp}')
print(f'{gen_comp}')

# Eu posso interar no genereators? sim!
gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)
