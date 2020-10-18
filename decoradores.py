"""
Decoradores - Decorators

oq são decorators???
- sãoa funções
- envolvem outras funções e aprimoram seus comportamentos
- tambem são exemplos de Higher Order Functions
- tem uma sintaxe propria, usando "@" (syntact sugar) é para deixar mais bonito, para declarar que é essa função


\................................................\
\                function decorator               \
\..................................................\
                 Função decorada


# Decorators como funções (sintaxe não recomendado/ sem açucar sintatico)

def educado(funcao): # function decorators
    def sendo():
        print(" Foi um prazer em conhece-lo")
        funcao()
        print("tenha um otimo dia")
    return sendo
def saudacao():
    print("seja bem vindo(a) a minha casa")

# testando 1

# teste = educado(saudacao)
#
# teste()

# teste 2

def raiva():
    print("TE ODEIO")

raiva_educada = educado(raiva) # Decorator

raiva_educada()

# Decorator syntax sugar

def sendo_educado(funcao):
    def sendo_mesmo():
        print(" Foi um imenso prazer em conhece-lo")
        funcao()
        print("Tenha um exelente dia")
    return sendo_mesmo

@sendo_educado
def apresentando():
    print(" Meu nome é Rebecca")

# teste
apresentando()

@sendo_educado
def dormir():
    print("Quero dormir")

dormir()

|............................................
|Home   | Serviços | produtos  | Administrativo
|.............................................

http://www.suaempresa.com.br/home

http://www.suaempresa.com.br/servicos

http://www.suaempresa.com.br/produtos

http://www.suaempresa.com.br/administrativo

# OBS: Não é codigo funcional, é apenas exemplos

def checa_login():
    if not request.usuario:
        redirect("http://www.suaempresa.com.br")

def home(request):
    return "pode acessar"

def servico(request):
    return "pode acessar"

def produtos(request):
    return "pode acessar"

@checar_login
def adim(request):
    return "pode acessar"

"""
# OBS: não confunda decorator com decorator function

