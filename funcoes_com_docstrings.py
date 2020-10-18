"""
Documenttando funçoes com docstrings

Podemos ter acesso da documentacao de uma funcao utilizando o metodo __doc_

Podemos ainda fazer acessso com a documentação help

"""
# Exemplo
def diz_oi():
    """Uma funcao simples q retorna oi"""
    return "oi"
print(diz_oi())
print(help(diz_oi()))

def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de numero
    :param numero: numero que desejamos gerar o exponencial
    :param potencia: potencia que queremos gerar o exponencial, por padrao é 2.
    :return: retorna o exponencial de um numero por potencia
    """
    return numero ** potencia
