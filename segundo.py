import primeiro
def funcao2():
    primeiro.funcao1()

if __name__ == "__main__":
    print("segundo.py esta sendo executado diretamente")
else:
    print(f"segundo.py importado {__name__}")