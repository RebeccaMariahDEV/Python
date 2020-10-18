"""
Escrevendo um iterador customizado

con = Contador(1,6)
it = iter(con)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
Um modo de fazer


"""
class Contador:
    def __init__(self, menor, maior): # função especide construtor
        self.menor = menor # self é para adicionar oa atributo um valor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration

for n in Contador(1, 61):
    print(n)

for i in range(1, 61):
    print(i)

"""
Podemos criar um interavel criando toda essa estrutura de dados para executar seu interavel

"""




