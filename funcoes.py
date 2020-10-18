"""
Definindo funções:
- Funções são pequenos trechos de codigo que realizam tarefas especificas
- Pode ou não receber entrada ou retornar saida de dados
- Muitos uteis para executar o precedimentos similares porrepetidas vezes:
- Funções são para não ter q repetir codigos


OBS: Se vc escrever uma função q realiza varias tarefas dentro dela:
é bom fazer uma verificação para que a função seja simplificada.


Já utilizamos
- print()
- len()
- max()
- min()
- sum()
- e muitas outras


"""
# # Exemplo de utulização
# cores = ["azul", "verde", "amarelo", "branco"]
#
# # utilizando a função integrada
# print(cores)
# nome = "rebecca: Mariah" # para str não tem append
# print(nome)
#
# cores.append("vermelho") # usado com dados estilo lista
# print(cores)
# cores.clear()# é uma função que não precisa entrar dados

# Como definir funções

"""
Em python a forma geral de definir uma função é:
def nome_da_função(parametro_da_função):
    bloco_de_função
    
    
Onde:
nome_da_função -> Sempre, com letra minuscula, se for nome composta,
separado por _
parametros_de_entrada -> opcionais, onde tendo mais de um, cada um separado por
virgula, sendo opcional ou não
bloco_da_função -> Tambem conhecido como corpo da função, é onde o processamento
da função acontece. Nesse bloco, pode ou não ter retorno na função.

OBS: Veja que para definir uma função, utilizamos a palavra reservada "def"
informamos em Python que estamos definindo um funcao. Tambem abrimos o 
bloco com o já conhecido dois pontos : que é utilizado em Python para definir blocos.

"""
# Definindo a primeira função
def diz_oi():
    print("oi")
"""
OBS:
1 - veja que, dentro das nossas funções podemos utilizar outras funçoes;
2 - veja q nossa função só executa uma tarefa
3 - veja que essa função nao recebe paraetros de entrada
4 - veja q essa função nao retorna nada

"""
# utilizando funções

# chamada de execução da função
diz_oi()

"""
Atenção: nunca esqueça de utilizar o parentese ao executar uma função

diz_oi errado
diz_oi() certo
"""
def cantar_parabens():
    print("parabens pra você")
    print("nessa data querida")
    print("muitas felicidades")
    print("muitos anos de vida")

for n in range(5): # loop de função
    cantar_parabens()
    print(n)

# em Pyton podemos criar variaveis do tipo de uma função e excutar essa função atravez da variavel
cantar = cantar_parabens # para criar tem q ser sem paranteses
cantar()
#isso não é comum
