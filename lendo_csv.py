"""
Lendo arquivos CSV - Comma separeted values

Podemos ter separador por virgula (1, 2, 3, 4, 5)
Podemos ter separador por ponto e virgula ( 1; 2; 3; 4; 5)
Podemos ter separador por espaço ("oi" "tudo" "bem" "?")

temos que ter um padrão para todo o arquivo, escolhendo separar nom um separador unico.

#Possível de trabalhar porem não ideal
with open('lutadores.csv') as arquivo:
    dados = arquivo.read()
    #print(type(dados))
    dados = dados.split(',')[2:]
    print(dados)

A linguagem python possui duas formas diferentes para ler aquivos csv:
- reader() -> permite que iteremos sobre as linhas do arquivo CSV como listas
- DictReader -> permite que interemos sobre as linhas do CSV como OrderedDicts


"""

# Reader
from csv import reader, DictReader

with open('lutadores.csv') as arquivos:
    leitor_csv = reader(arquivos)
    next(leitor_csv) #pula a primeira linha
    for linha in leitor_csv:
        #cada linha é uma lista
        print(f'{linha[0]} nasceu no(a)(s) {linha[1]} e mede {linha[2]} centímetros')
#isso serve para x linhas que vc quiser
print('\n')

with open('lutadores.csv') as arquivos:
    leitor_csv = DictReader(arquivos)
    for linha in leitor_csv:
        #cada linha é um dict
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['Pais']} e mede {linha['Altura (em cm)']} centímetros")

"""
Caso eles não utilizassem a ',' para separar era só utilizar ex:  leitor_csv = DictReader(arquivos, delimiter =',')
"""