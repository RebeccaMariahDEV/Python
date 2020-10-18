"""
Podemos adicionar estruturas condicionais logicas as nossas list comprehensions

"""
# Exemplo 1
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = [ numero for numero in numeros if numero % 2 == 0]
impar = [ numero for numero in numeros if numero % 2 != 0]
print(pares)
print(impar)

# Refatorando
pares = [numero for numero in numeros if not numero % 2]
# qualquer numero dividido pelo restante (%) de 2 é 0 sendo 0 falso, not false = True

impar = [numero for numero in numeros if numero % 2]
# Qualquer numero impar dividio pelo restante de 2 sobra 1 oq é True

print(pares)
print(impar)
# exemplo 2
res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)