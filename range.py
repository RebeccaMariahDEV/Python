"""
precisamos conhecer os loops para usar o range
ranges sao utilizados para gerar sequencias numericas, nao de forma aleatoria,
mas de maneiras especificas

forma de range
for num in range(11):
    print(num) #comeca em zero e para em 10

forma de range 2
for num in range(1,11):
    print(num) # comeca em 1 e para em 10

forma de for 3
for num in range(1, 10 , 2): # ele vai contar de 2 em 2 numeros
    print(num) # o ultimo numero depois da virgula fala de quantos em quantos numeros vai contar

exemplo de for 4
for num in range(10, 0, -1): # forma de contar de traz para frente e vice e verca
    print(num)

"""

# while tambem é um loop

"""
while é uma expressao booleana em loop

exemplo de while 1
numero = 1

while numero < 10:
    print(numero)
    #numero = numero + 1 # cuidado para nao entrar em loop infinito
    
exemplo 2

numero = ""

while numero != "sim":
    numero = input("ja acabou jessica?! ")
    
"""

# numero = ""
#
# while numero != "sim":
#     numero = input("ja acabou jessica?! ")

# break's

"""
o break serva para sair de loops de maneiras projetadas

"""

for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print("Sair do loop")

while True:
    comando = input("Digite sair para sair ")
    if comando == "sair":
        break