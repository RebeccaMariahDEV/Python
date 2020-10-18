"""
Modulo collections - Default Dict
#OBS: tudo que vimos no dicionario serve para Default dict

dicionario = {"Rbecca Mariah Avelino": "Mozi Mussi"}
print(dicionario)
print(dicionario["Rbecca Mariah Avelino"])
print(dicionario[cacau]) # ??? Se nao conter a chave dara erro

Default dict -> Ao criar um dicionario usando o default dict, nos informamos
um valor default, podemos utilizar um lambda para isso. Este valor sera utilizado
sempre que nao houver um valor definido. Caso tentemos acessar uma chave q nao
existe essa chave sera criada e o valor default sera atribuido.

OBS: - Lambda são funcoes sem nome, que pode ou nao receber parametros de entrada
e retornar valores

from collections import defaultdict
dicionario = defaultdict(lambda: 0)
# print(dicionario)
dicionario["Cacau"] = "Pet do mussi"
print(dicionario)
print(dicionario["Rbecca"]) # em outro dict isso daria erro, pelo default nao
print(dicionario)


"""

