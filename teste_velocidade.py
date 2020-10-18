"""
Teste de velocidade com expressões geradoras

# Generators
def num():
    for n in range(1,10):
        yield n
g1 = num()
print(g1)
print(next(g1))

# generator expression
g2 = (num for num in range(1,30))
print(g2)
print(next(g2))


"""
# teste de velocidade
import time

# generator expression
gen_inicio = time.time()

print(sum(num for num in range(100000000)))
gen_tempo = time.time() - gen_inicio

# list comprehension
list_inicio = time.time()
print(sum([num for num in range(100000000)]))
list_tempo = time.time() - list_inicio

print(f"Generator expression levou {gen_tempo}")
print(f"List comprehension levou {list_tempo}")
