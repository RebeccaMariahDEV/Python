"""
POO:
    - Classes:
Em POO Classes nada mais são do que modelos dos objetos do mundo real representados computacionalmente

Imagne que vc queira fazer um sistema para automatizar as lampadas da sua casa

Classes podem conter:
    - Atributos -> representam as caracteristicas do objjeto, pelos atributos consequimos
    representar computacionalmente os estados do objeto. No caso da lampada por ex, possivelmente
    iriamos querer saber se a lampada é 110 ou 220 volts, sua cor, qual a luminosidade dela etc.

    - Metodos(funções) -> representam os comportamentos do  objeto, ou seja, as ações que este objeto
    pode realizar no seu sistema, no caso da lampada, um comportamento comum que muito provavelmente
    iriamos querer representar no sistema é o de ligar e desligar a mesma.

Em python, para definir uma classe utilizamos a palavra class e o nome da sua classe em MAIUSCULO com :

OBS: utilizamos a palavra pass quando temos um bloco de codigo quando não implementamos o bloco
- Quando nomeamos nossas classe em python, utilizamos por convenção o nome inicial em maiusculo,
se for composto colocamos ambos os nomes em letra maiuscula e juntas

Dica: em computação não utilizamos acentuação, espaços, coracteres ou ect, para nomes de classes,
atributos, metodos, arquivos, diretorios etc.

OBS: quando estamos planejando um sistema e definimos quais classes vamos ter, chamamos estes
objetos que serão mapeados para classes de entidade.
"""


class Lampada:
    pass

lamp = Lampada()



print(type(lamp))