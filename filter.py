"""
Filter
A função filter serve para filtrar dados de uma determinada coleção

#Biblioteca para trabalhar com dados estatisticos
import statistics
# dados coletados
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

#Calculando a media dos dados utilizando a função mean()
media = statistics.mean(dados)
print(media)
#Obs: assim como a func map a filter recebe dois parametros, sendo 1 func e 2 interavel
res = filter(lambda valor: valor > media, dados)
print(list(res))
print(f"novamente:{list(res)}")
#OBS: Assim como na função map, apos ser utilizados os dados de filter eles são apadados da memoria
print(type(res))

#REmoção de dados faltando
paises = ["", "brasil", "chile", "", "australia", "", "", " equador", "argentina"]
print(paises)

print(list(res))

res = filter(lambda pais: len(pais) >0, paises)
# ou
res = filter(None, paises)
# Ou
res = filter(lambda pais: pais != "", paises)
print(list(res))

OBS: A diferenção entre map e filter é:
na map recebe dois parametros, uma func e um interavel e retorna um objeto mapeado a func para cada elemento
filter: recebe dois parametros, uma func e um interavel e retorna um objeto filtrado apenas os elementos de acordo com a func


"""
# Exemplo mais complexo
usuarios = [
    {"username": "rebecca", "twets":["fã de pizza", "me sinto o rafael das tn"]},
{"username": "marcel", "twets":["fã de pizza", "me sinto o rafael das tn", "odeio segundas"]},
{"username": "bruna", "twets":[]},
{"username": "lucca", "twets":["fã de pizza", "me sinto o rafael das tn", "adoro bolos"]},
{"username": "hilary", "twets":["fã de pizza"]},
{"username": "gal", "twets":[]}
]
#Filtrando usuarios inativos do tt
inativos = list(filter(lambda u: len(u["twets"]) == 0, usuarios))
print(inativos)
ativos = list(filter(lambda u: len(u["twets"]) >= 1, usuarios))
print(ativos)

# forma 2
inativos = list(filter(lambda usuario: not usuario["twets"], usuarios))
print(inativos)
# uma lista vazio transformado em bool é falso, por isso o not

# Como combinar filter e map
nomes = ["vanessa", "ana", "maria"]
#devemos criar uma lista contendo 'sua instrutora é' + nome, desde que cada nome tenha 5 caracteres
lista = list(map(lambda nome: f'sua instrutora é {nome}', filter(lambda nome: len(nome) <= 5, nomes)))
print(lista)

