"""
Forçando tipos de dados com decoradores

Zip -
pega duas tuplas e converte em uma
( 1, 3, 5)
(2, 4, 6)
c = zip(a, b)
c fica (1, 2) (3, 4) (5, 6)


"""
# Exemplo
def forca_tipo(*tipos):
    def decorador(funcao):
        def converter(*args, **kwargs):
            novo_args = []
            for (valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))
            return funcao(novo_args, **kwargs)
        return converter
    return decorador

@forca_tipo(str, int)
def repetr_msg(msg, vezes):
    for vez in range(int(vezes)):
        print(msg)

repetr_msg("OI amor", "5")

@forca_tipo(float, float)
def dividir( a, b):
    print(a/b)

print(dividir(5, 6.8))