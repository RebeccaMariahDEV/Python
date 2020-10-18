"""
and, or, not, is. sao operadores (not é unarios) (and , is e or sao binarios)
"""
# Loops
"""
nume = "Rebecca Mariah # uma STR
lista = [1, 2, 3, 4, 5, 7, 9] # LISTA
numeros = range(1,10) # Forma de RANGE

nome = "Rebecca Mariah"
lista = [1, 2, 3, 4, 5, 7, 9]
numeros = range(1,10)
for letra in nome:
    print(letra)

# exemplo de for 2:
for numero in lista:
    print(numero)

# for 3 (interando em um range) 
#Range vc usa o valor inicial e o final, porem o final nao é inclusive.
for numero in range(1,20):
    print(numero)
    
#for 4

# for i, v in enumerate(nome):
#     print(i , v)

#for 5

for _, letra in enumerate(nome): # quando nao precisa do valor das letras é so utilizar o _
#     print(letra)

# for 6


for n in range(1, qtd + 1):
    num = int(input(f" informe o {n}/{qtd} valor: ")) # aqui o n e o numero da fracao total que é a qtd
    soma += num
print(f"a soma é {soma}")

"""
nome = "Rebecca Mariah"
lista = [1, 2, 3, 4, 5, 7, 9]
numeros = range(1,10)
v = enumerate(nome)

#
#
#
# qtd = int(input("Quantas vezes quer que esse loop aconteca? "))
# soma = 0
# for n in range(1, qtd + 1):
#     num = int(input(f" informe o {n}/{qtd} valor: ")) # aqui o n e o numero da fracao total que é a qtd
#     soma += num
# print(f"a soma é {soma}")

# podemos concatenar varias coisas ex: nome = Rebecca
# nome + mariah
#saira nome = Rebecca Mariah

"""
modificando caracteres de emoji
primeiro prescisamos do emoji universal da linguam de programacão
original U+1F60D
modificado U0001F60D

"""
"U0001F60D"
for _ in range(3):
    for num in range(1, 11):
        print(" \U0001F48F" * num, "te amo")
        # tipo de utilizacao do for