"""
POO - metodos magicos

São todos os metodos que utilizam dunder,
ex: __init__ (sonstrutor)
__repr__ (representação do objeto)
__str__ (mostra o objeto em str)
__len__ (mostra o tamanho que vc quiser mostra)
__del__ (deleta os objetos da memoria)


"""
class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self): # é para o dev
        return f"{self.titulo} do autor {self.autor}"

    def __str__(self):
        return self.titulo

    def __len__(self):
        return self.paginas

    # def __del__(self):
    #     print("um objeto do tipo livro foi deletado da memoria")

    def __add__(self, outro):
        return f" {self} - {outro}"

li1 = Livro("as aventuras de juca pirama", "Eneias", 180)
li2 = Livro("como eu era antes de você", "não sei", 340)
print(li1)
print(li2)
print(len(li1))
print(len(li2))
print(li1 + li2)