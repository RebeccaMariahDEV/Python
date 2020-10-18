"""
Any e All

all() -> retorna True se todos os elementos do interavel são verdadeiras ou ainda se o interavel esta vazio

# Exemplo all()
print(all([0,1,2,3,4])) # todos os elementos são verdadeiro? False
print(all([1,2,3,4])) # aqui dara True
print(all([])) # aqui dara True tbm
print(all((1,2,3,4))) # True
# pode ser usado em tupla, lista, set e com str

nomes = ["carlos", "camila", "carla", "cassio"]
print(all([nome[0] == "c" for nome in nomes]))
# Aq é um exemplo que pode ser sobre qualquer coisa

OBS: interavel vazio convertido em boolean é falso, mas o all() entende como True
print(all([letra for letra in "eio" if letra in "fpk"]))
#gera um interavel vazio aq oq é true

print(all([num for num in [2, 4, 6, 8] if num % 2 == 0]))

Any() -> retorna True se qualquer elemento do interavel for verdadeiro, se o interavel estiver vazio retorna falso
Se qualquer um for verdadeiro aqui dara True, mesmo se tiver outros falsos no meio

"""
print(any([0, 1, 2, 3, 4])) # True
print(any([0, False, {}, (), []])) # False
print(any([0, False, {}, (), 4])) # True

nomes = ["carlos", "camila", "carla", "cassio"]
print(any([nome[0] == "c" for nome in nomes]))
print(any([num for num in [2, 4, 10, 6, 8] if num % 2 == 0]))
