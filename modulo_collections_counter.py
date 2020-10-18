"""
Modulo collections: - Counter(contador)
collections -> high performance container detetypes

Counter -> Recebe um interavel como parametro e cria um objeto do tipo collections counter,
que é parecido com um dicionario, contendo  como chave o elemento da lista, e
como valor a quantidade de ocorrencias desse elemento
# Realizando um import

from collections import Counter

#Exemplo 1

#Podemos usar qualquer interavel, aqui usamos uma lista
lista = [2, 4, 5, 67, 890, 45, 3, 56, 2, 32, 12, 234567, 3, 3, 3, 5, 5, 5, 5, 0, 5, 3]

# Utilizando o Counter
res = Counter(lista)
print(res)
print(type(res))
Counter({5: 6, 3: 5, 2: 2, 4: 1, 67: 1, 890: 1, 45: 1, 56: 1, 32: 1, 12: 1, 234567: 1, 0: 1})
# Veja que para cada elemento da lista, o Counter criou uma chave e colocou como valor
#o numero de vezes q ele aparece na lista

# Exemplo 2
print(Counter("Rebecca Mariah Avelino"))


"""
from collections import Counter

# Emeplo 3
texto = """
Dá-me a tua mão

Dá-me a tua mão:
Vou agora te contar
como entrei no inexpressivo
que sempre foi a minha busca cega e secreta.
De como entrei
naquilo que existe entre o número um e o número dois,
de como vi a linha de mistério e fogo,
e que é linha sub-reptícia.

Entre duas notas de música existe uma nota,
entre dois fatos existe um fato,
entre dois grãos de areia por mais juntos que estejam
existe um intervalo de espaço,
existe um sentir que é entre o sentir
– nos interstícios da matéria primordial
está a linha de mistério e fogo
que é a respiração do mundo,
e a respiração contínua do mundo
é aquilo que ouvimos
e chamamos de silêncio
"""
palavras = texto.split()
print(palavras)
res = Counter(palavras)
print(res)

# Encontrando as 5 palavras mais utilizadas no texto
print(res.most_common(10))