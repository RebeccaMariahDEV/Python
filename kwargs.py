"""
Entendendo o **kwargs

Ele sempre é com duplo asterisco
O nome dele foi definido pela comunidade
Este é só mais um parametro, porem ele é diferente do args que coloca os valores em tuplas,
o **kwargs exige que utilizemos parametros nomeados, e transformas os extras em um dict.

"""
# Exemplo
def comidas_favoritas(**kwargs):
    print(kwargs)

comidas_favoritas(Marcelo="lasanha", cacau="whiskas", rebecca="japones")
def comida_favorita(**kwargs):
    for pessoa, comida in kwargs.items():
        print(f"{pessoa} {comida}")

"""
Como o kwargs é um dict usamos o .items() para adicionar ao nome da pessoa
lembrando: para iniciais maiusculas utilizar o .title() no print

OBS: os parametros *args e **kargs não são obrigatorios

"""
comidas_favoritas(daniella="frango frito")

#Exemplo mais complexo
def cumprimento_especial(**kwargs):
    if "geek" in kwargs and kwargs["geek"] == "python":
        return "Você recebeu um cumprimento pythonico"
    elif "geek" in kwargs:
        return f" {kwargs ['geek']} Geek!"
    return "não tem"
print(cumprimento_especial(geek="python"))
print(cumprimento_especial(geek="oi"))

"""
Lembra: kwargs trabalha como dict

Nas nossas funções podemos ter:
- parametros obrigatorios
- parametros args
- parametros default ( que não são obrigatorios)
- parametros kwargs
Sendo nessa ordem

"""
def minha_funcao(nome, idade, *args, solteira=False, **kwargs):
    print(f"{nome} tem {idade}")
    print(args)
    if solteira:
        print("Solteira")
    else:
        print("Casada")
    print(kwargs)

print("rebecca", 24)
#print("marcelo", 29, 3, solteira=True)
print("daniella", 28, "não")
#print("antonia", 19, 6, True, pyhton=False)

#Ordem correta
def mostra_info(a, b, *args, aluno="presente", **kwargs):
    return [a, b, args, aluno, kwargs]
print(mostra_info(1, 2, 3, aluno="rebecca", sobrenome="mariah"))

# ordem errada
def nova_funcao(a, b, aluno="rebecca", *args, **kwargs):
    return [a, b, aluno, args, kwargs]
print(nova_funcao(1, 2, 3, sobrenome="mariah", profisao="atleta"))

# Desempacotando com kwargs
def nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {"nome":"bruna", "sobrenome":"surfistinha"}
print(nomes(**nomes))

"""
A partir do duplo asterisco desempacota o dict
para desempacotar lista, tupla, set pode usar o asterisco simples tambem
OBS: os nomes das chaves em um dict deve ser o mesmo dos parametros da função
"""
