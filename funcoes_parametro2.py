"""
Funções com parametros padroes (Default paramters)

- Funções onde a passagem de parametro é opcional:
# Exemplo:
print("OI, Bom dia")
print()
# é execultado normalmente, sem erros

# Exemplo de funções com parametros obrigatorios
def quadrado(numero):
    return numero **2
print(quadrado(5))
# passagem de parametro obrigatorio

def exponencial(numero, potencia = 2):
    return numero ** potencia
print(exponencial(5,7))
print(exponencial(6))
# Se colocar um valor a um parametro, o seu argumento vai se tornar opcional

#OBS: os parametros com valores default (padrao) devem sempre estar ao final da declaração

# Erro
def teste(num = 2, potencia):
    return num ** potencia
print(teste(6)) # o valor 6 foi para num e potencia fica com nada, dara erro

# Outros exemplos
def soma(a,b):
    return a +b
print(4,7)
print(soma(7))# Erro
print(soma())# Erro
# Ambos os parametros são obrigatorios

# Exemplo mais complexo

def mostra_informacao(nome="rebecca", atleta=False):
    if nome == "rebecca" and atleta:
        return "Bem vindo"
    elif nome == "rebecca":
        return "pensei que tu era a rebecca"
    return f"Ola {nome}"
print(mostra_informacao())
print(mostra_informacao(atleta=True)) # tem que colocar o nome do parametro para direcionar o dado
print(mostra_informacao("Rebecca"))
print(mostra_informacao("Marcelo"))

Porque utilizar parametros com valor default
- Nos permite ser mais flexiveis nas funçoes
- Evita erros nos parametros incorretos
- nos permite trabalhar com exemplos mais legiveis de codigos

# tipos dedados para parametros default
- Qualquer tipo de dados
    - numeros, str, float,bool,list,tuple,dict,def etc

# Exemplos:
def soma(num1, num2):
    return num1 + num2
def mat(num1, num2, fun=soma):
    return fun(num1, num2)

def subtração(num1, num2):
    return num1 - num2

print(mat(2,3))
print(mat(2,2, subtração))

# Funções usando outras funçoes

# Escopo - Evitar problemas e confucoes

# variavel global
# variavel local

instrutor = "geek" # Variavel global

def diz_oi():
    instrutor = "Python"
    return f"oi {instrutor}"
print(diz_oi())

# Se houver uma variavel com o mesmo nome da variavel local, a local tera preferencia e sera utilizada

def diz_oi():
    prof = "Ana" # Variavel local
    return f"Ola {prof}"
print(diz_oi())
print(prof) # name error

# Se puder evitar variaveis globais evite
total = 0
def incremento():
    total = total + 1 # dara erro, pois a local nao foi declarada
    return total
print(incremento())

# Correto
total = 0
def incremento():
    global total # Avisamos que queremos usar a variavel global
    total = total + 1
    return total
print(incremento())
print(incremento()) # a cada vez que utilizar somara + 1


"""
# Podemos ter funçoes declaradas dentro de funcoes
# Tendo uma forma expecial de escopo de variavel

def fora():
    contador = 0
    def dentro():
        nonlocal contador #não é local e nem global, é a variavel da função acima
        contador = contador + 1
        return contador
    return dentro()
print(fora() * 3)
print(fora())

#





