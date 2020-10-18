"""
Modulo Collections: Ordered Dict

#Em um dict a ordem nao é garantida, por se organizar automaticamente

diionario = { "a": 1, "b":2, "c":7, "h": 56} # dict comum
for chave, valor in diionario.items():
    print(f' {chave} e {valor}')

# fazendo o import
from collections import OrderedDict
dicionario = OrderedDict({"a": 3, "b": 6, "d": 2, "s": 4 })
for chave, valor in dicionario.items():
    print(f"chave = {chave} e valor = {valor}")
# OBS: com OrderedDict é um dicionario que garante a orde de criação


"""
# Entendendo a diferença de dict e ordered dict
from collections import OrderedDict

# Dict comum
dicionario1 = {"a": 1, "b": 2}
dicionario2 = {"b": 2, "a": 1}

print(dicionario1 == dicionario2) # Retorna True
# Para o dict comum não importa a ordem, apenas valor

# Ordered dic
odict1 = OrderedDict({"a": 1, "b": 2})
odict2 = OrderedDict({"b": 2, "a": 1})
print(odict1 == odict2)# Retorna False
# Em um Ordered dict a orde altera o dict o tornando diferente

