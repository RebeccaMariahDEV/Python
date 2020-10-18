"""
Dunder main = __main__
Dunder name = __name__

Tem varios metodos utilizando dunder

Em pynthon são utilizados para criar funções, atributos, propriedades etc;
 utilizando dunder para não gerar confito com o nome desses elementos

# Em python se executarmos um modulo python diretamente na linha de comando, internamente o python
atribuia a variavel __name__ ao valor __main__ indicando que este modulo é o modulonde execução principal

Main -> siginifica principal

"""
from funcoes_com_parametros import soma_impares

print(soma_impares([1, 2, 3, 4, 5, 6, 7, 8, 9]))

import primeiro
import segundo
