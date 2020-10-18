"""
Sã0 c0nhecidos como dict's
Dict's sao representados por {}

# Formulas de interar sobre dict's

receita = {"jan": 20, "fev": 35, "mar": 24, "abr": 65 }
print(receita)

# Interar sobre dict
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f"{chave}: {receita[chave]}")

 # ou dessa forma
É uam forma de acessar as chaves direto

print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

# Acessando os valores direto:
print(receita.values()) # Modo pythonico
for valor in receita.values():
    print(valor)

# Desempacotamento

print(receita.items())
for chave, valor in receita.items():
    print(f"{chave} e {valor}")

# Sum, max, min, len; OBS: só podemos usar esse metodos se os valores forem int ou float
# Só é utilizavel em valores
print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita.values()))
print(len(receita)) # pode usar para numero de valores ou chaves e pelo dict inteiro,
# Se o mesmo tiver mais valores dq chaves e por ai vai

"""
receita = {"jan": 20, "fev": 35, "mar": 24, "abr": 65 }
print(receita)
