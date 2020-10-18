"""
O bloco With

É utilizado para criar um contexto de trabalho, onde os recursos utilizados são fechados apos o bloco whith

"""

# o bloco with

with open("texto.txt") as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)
# Forma pythonica de manipular arquivos

print(arquivo.closed)