"""
O bloco Try/ Except

utilizamos ele para tratar erros no nosso codigi, previnindo que o programa pare de funcionar e o usuario receba
mensagens de erros inesperadas.

A forma geral: mais simples é:
Try:
    // execução problematica

except:
    // o que deve ser feito em caso de problema

"""
try:
    geek()
except:
    print("deu ruim em")

# aqui o programa rodou, pq colocamos um tratamento para ele mostrar,
# oq é bom para não travar, mas mostrar o pq não funciona
"""
OBS: tratar erros de forma generica não resolve, sempre tente expecificar os erros

"""
# Exemplo
try:
    geek()
except NameError:
    print("Essa função não existe")

    # Exemplo 2
try:
    len(6)
except NameError:
    print("Não funciona") #errado
#correto
except TypeError:
    print("Tipo errado")#certo

# ou 3
try:
    len(3)
except TypeError as err:
    print(f"A aplicação gerou um erro tipo {err}")

"""
Porem existe casos com diferentes tipos de erros
"""
try:
    len(0)
except NameError as erra:
    print(f"Deu NameError: {erra}")
except TypeError as errou:
    print(f"Não funcionou por {errou}")
# Dessa forma mostra exatamente o erro é especifica o seu erro

# outro exemplo

def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
dic = {"nome": "bruna"}

print(pega_valor(dic, "bruna"))

print(pega_valor(dic, "game"))
# como tem tratamento os erros não travam o programa
