"""
try/ except/ else/ finally

Quando e onde tratar o codigo:
- Toda entrada deve ser tratada!!!

OBS: A função do usuario é destruir seu sistema

# Else -> é executado somente se não ocorrer o erro

try:
    num = int(input("Informe um numero: "))
except ValueError:
    print("certeza que é um numero?! ")
else:
    print(f" Você digitou {num}")

# Finally

try:
    num = int(input("Valor: "))
except ValueError:
    print("Valor não definido")
else:
    print(f"numero {num} ")
finally:
    print("Executando o finally") # quase inutio

# O bloco finally é Sempre executado, independente se houver execução ou não
# Ele geralmente é utilizado para fechar ou deslocar recursos

# Exemplo errado
def dividir(a, b):
    return a/b

num1 = int(input("primeiro numero: "))
try:
    num2 = int(input("segundo valor: "))
except ValueError:
    print("o valor tem q ser numerico")

try:
    print(dividir(num1,num2))
except NameError:
    print("Valor incorreto")


"""
# Exemplo certo
#OBS: Você é responsavel pelas suas funções, entao trateas
# toda entrada deve ser validada

def dividir(a, b):
    try:
        return int(a)/ int(b)
    except ValueError:
        return "valor incoreto"
    except ZeroDivisionError:
        return " não é possivel dividir por zero"


num1 = int(input("primeiro numero: "))
num2 = int(input("segundo valor: "))

print(dividir(num1, num2))