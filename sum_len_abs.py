"""

Len, Abs, Sum, Round

Len-> retorna o numero de itens de um interavel
# Por debaixo dos panos, quando utilizamos a funcao len() o python faz o seguinte
print("oi"._len_()) # isso e um dander, que sao funcoes especiais que atende a varios outros objetos

Abs -> retorna o valor absoluto de um numero inteiro ou real, de forma basica e o valor real sem o sinal
#exemplo
print(abs(-5))
print(abs(3.14)) #retorna tudo positivo, nao pode utilizar abs de str

Sum -> recebe como parametro um interavel podendo receber um valor inicial, e retorna o valor total dos elementos incluindo o inicial
OBS: o valor inicial defaul e 0
print(sum([1,2,3,4,5]))
print(sum([1,2,3,4,5], 5))# o , 5 e o valor default, que e somado aos outros valores
Lembre que nao soma dicionarios sem o .values() no fim do dicionario.

Round -> retorna um numero aredondado para n digito de precisao apos a casa decimal; se a precisao nao for informada retorna o inteiro mais proximo da entrada
#Exemplo
print(round(3.14))
print(round(45.7986876656, 2))# duas casa de precisao
Ate 0.5 ele aredonda para baixo, 0.6 aredonda para cima

"""
print(round(45.76888, 2))
print(abs(-5))
print("Rebecca mariah"._len_())
print(sum({"a": 2, "c": 78, "h":8}.values()))