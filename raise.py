"""
Levantando os proprios erros com raise

Raise -> Lança exeções
OBS: ele não é uma função, ele é uma palavra reservada, assim como def, para simplificar pense nele como um meio
para criar nossas proprias mensagens de erros ou tipos

# Exemplo

def cores(texto, cor):
    if type(texto) is not str:
        raise TypeError("testo tem que ser em str")
    if type(cor) is not str:
        raise ("cor tem que ser em str")
    print(f"o texto{texto} sera impresso em cor{cor}")

cores("True", 7)
"""

# Exemplo

def cores(texto, cor):
    cores = ("verde", "azul", "vermelho", "preto", "roxo")
    if type(texto) is not str:
        raise TypeError("testo tem que ser em str")
    if type(cor) is not str:
        raise ("cor tem que ser em str")
    if cor not in cores:
        raise ValueError(f"A cor precisa ser uma entre: {cores}")
    print(f"o texto {texto} sera impresso na cor {cor}")

cores("Rebecca", "roxo")
