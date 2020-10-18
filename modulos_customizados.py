"""
Modulos customizados

Como modulos pythons são arquivos pythons, então todos os programas/ arquivos são modulos pythons,
prontos para serem utilizados.

Exwmplo

from funcoes_com_parametros import soma_impares

print(soma_impares([1, 2, 3, 4, 5, 6, 7, 8, 9]))
importando uma função expecifica do nosso modulo


"""
# Importando todas as funções do nosso modulo
import funcoes_com_parametros as fcp

print(fcp.lista)
# estamos acessando e imprimindo uma variavel contida no modulo


print(fcp.soma_impares(fcp.lista))
