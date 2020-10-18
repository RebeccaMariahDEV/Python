"""
Entendendo o Args
- O asterisco args é um parametro com outro qualquer , isso significa que você podera
chamar de qualquer coisa, desde que comeca com arterisco.
Exemplo: poderiamos chamar de asterisco x, mas a comunidade adotou o nome args para definilo
Mas oq é args???
- o parametro args é utilizado em uma função, coloca os valores extras informados como entrada
em uma tupla. Então desde ja lembre-se que tuplas são  imutaveis.


"""
# Exemplo
def soma_numeros(num1, num2, num3):
    return num1+num2+num3
# Aq temos 3 parametros e só pode passar 3 valors para execultar corretamente essa função sem erro
print(soma_numeros(4, 5, 8))

# Usando o args
def soma_numeros1(*args):
    return  sum(args)
# Com o args você pode passar quantos parametros quiser
print(soma_numeros1(4, 6, 2, 8, 9))
# Só soma se for valores reais

def verifica_info(*args):
    if "Rebecca" in args and "atleta" in args:
        return"Bem vinda"
    return"Não indentificado"
print(verifica_info(1, True, "Rebecca", "atleta"))
# o 1 e o True aq são insignificantes, pois a verificaão é se conterm a rebecca e o atleta,
#porem ele aceita sem erros

"""
Podemos tambem usar uma lista de dados ou uma tupla, porem ele sera desempacotado
poremusando *e o nome da lista outupla

"""
numeros = [ 1, 2, 3, 4, 5, 6, 7, 8]
print(soma_numeros1(*numeros))
number = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(soma_numeros1(*number))

# O * serve para informar que estamos passando como argumento uma coleção de dados,
# dessa forma ele sabera que precisa desempacotar esses dados ( tupla e lista, sendo numeros reais)
