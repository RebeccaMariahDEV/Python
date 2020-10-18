"""
Orientação a Objetos

Ela mapeia objetos do mundo real para colocar na programação
- Pensar em como modelara ele e como utilizar
- Para os objetos temos classes para cada um deles

EX Classe: - Produto -> preço, nome, desconto

POO -> é um paradigma de programação, que utiliza objetos do mundo real para modelos computacionais
-> Paradigma de programação é a forma/metodologia utilizada para pensar/desenvolver sistemas

Principais elementos da Orientação a Objetos:
Classe: modelo do mundo real sendo representado computacionamente
Atributos: caracteristicas do objeto
Metodo: comportamento do objeto (função)
Construtor: metodo especial utilizado para criar objetos
Objeto: instancia da classe, ex: caneta, produto final a partir da sua classe


"""
class Produto:
    pass
ps4 = Produto() #construtor, ps4 é um objeto da classe produto
print(ps4)
print(type(ps4))
# a partir do momento que criamos uma classe temos um novo tipo de dado que é o produto
