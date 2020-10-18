"""
Recebendo dados do usuario
"""
print("Qual seu nome: ")
nome = input()
print("Qual a sua idade?: ")
idade = input()
# processamento

#o processamento pode ser feito em uma linha so ex:
idade = int(input("Qual sua idades?: "))

#saida de dados

print("Seja bem vindo(a) {0}" .format(nome, idade))
# mais atual
print(f"Seja bem vindo(a) {nome}")
print(f"A {nome} nasceu em {2018 -(idade)}")
#como calcular o ano que a pessoa nasceu pelo ano atuar - a idade dela


# __buitins__ é um recurso integrado de dados
# a % vai subistituir a variavel que vc quer usar
# exemplo de print antigo:
# print("Seja bem vindo(a) %s" %(nome, idade))
# atual é
# print("A {0} tem {1} anos" .format(nome, idade)) [essa é nas versoes mais modernas]
# mais atual de todos é
#print(f"A {nome} tem {idade} anos")