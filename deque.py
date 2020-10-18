"""
Modulo Collections: Deque

Podemos dizer que o deque é uma lista de alta performace


"""
# imort
from collections import deque

#Criando deques
deq = deque("Cacau")
print(deq)

# Adicionando elementos em um deque
deq.append("Mussi") # adiciona no final da lista
print(deq)
deq.appendleft("Rbecca")# adiciona no começo da lista
print(deq)

#Removendo elemntos
print(deq.pop())# remove e retorna o ultimo elemento
print(deq)
print(deq.popleft()) # removera o primeiro da lista
print(deq)


