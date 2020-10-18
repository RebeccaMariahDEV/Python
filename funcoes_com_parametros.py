"""
Funções com parametro de entrada:
- funções que recebem dados para serem processados dentro da mesma

se pensarmos em um programa qualquer, geralmente temos isso:
entrada, processo e saida
se pensar em funções é:
já sabemos que funçoes não nescessariamente possuem entrada ou saidas,
ou não recebe entrada ou saida e por ai vai

# Refatorando uma função
def quadrado(numero): # essa função recebe um parametro, se tornando obrigatorio para executar
    # return numero *numero ou outro tipo
    return numero ** 3

print(quadrado(2))
print(quadrado(6))
print(quadrado(5))
# secolocamos sem o parametro dara erro: typeError

# refatorando a função
def cantar_parabens(aniversariante):
    print("parabens pra você")
    print("nessa data querida")
    print("muitas felicidades")
    print("muitos anos de vida")
    print(f"parabens {aniversariante}")

cantar_parabens("rebecca")


"""
# Funções podem ter n parametros de entrada, ou seja, podemos receber como entrada
# em uma função quantos parametros forem nescessarios separados por virgulas

# exemplo 1
# def soma(a, b):
#     return a + b
#
# def multiplica(num1, num2):
#     return num1 * num2
#
# def outra(num1, b, msg):
#     return (num1 + b) * msg
#
# print(soma(7, 6))
# print(multiplica(4, 8))
# print(outra(6, 7, "Teste"))
#
# # Obs: Se informar um numero errado de paramentro, ou argumentos, dara TypeError
#
# def nome_completo(nome, sobrenome):
#     return f"Seu nome completo é {nome} {sobrenome}"
#
# print(nome_completo("Rebecca", "Mariah"))
#
# #A diferença entre parametros e argumentos:
# # - parametros sao variaveis declaradas em uma função;
# # - argumentos sao dados passados durante a execulção de uma função
#
# # A ordem dos parametros importa
# nome = "Arthur"
# sobrenome = "Mariano"
#
# print(nome_completo(sobrenome, nome))
#
# # Argumentos nomeados: conhecido na programação por keyWord Arguments:
# # Caso  utilizemos nomes dos parametrosno nos argumentos para informalos,
# # podemos utilizar qualquer ordem
#
# print(nome_completo(nome= "Rebecca", sobrenome= "Mariah"))
# # ou
# print(nome_completo(nome= nome, sobrenome= sobrenome))
# # ou
# print(nome_completo(sobrenome= "Marques", nome= "Marcia")) # KeyWord Arguments

# erro comum na utilização do return

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0: # se quiser usar o return no if dara 1 e acabara, como quero ver toda a lista o retur é no for
            total = total + num
    return total

if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5, 6, 7]
    print(soma_impares(lista))


