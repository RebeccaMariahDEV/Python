"""
Modulos Externo

Utilizamos um pacote de modulos internos chamado PIP

Colorama
- Ele é utilizado para permitir impreção de texto no terminal
- É um modulo de brincadeira para colorir textos

# Exemplo

from colorama import Fore, Back, Style
init()
print(Back.YELLOW + " Oi")
print(Style.DIM + " Cacau")
print(Fore.YELLOW + " Nescal")
print(Fore.BLACK + "Rebecca")

Pacote pdf do python


"""
import pydf
pdf = pydf.generate_pdf('<h1>this is html</h1>')
with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)