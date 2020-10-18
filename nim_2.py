def usuario_escolhe_jogada(n,m):
    jogador = False
    while not jogador:
        tirar = int(input("Quantas peças dejesa tirar?"))
        if tirar > m or tirar < 1:
            print("Opcao errada")
        else:
            jogador = True
    return tirar

def computador_escolhe_jogada(n,m):
    computador_tira = 1
    while computador_tira != m:
        if (n - computador_tira) % (m +1) == 0:
            return computador_tira
        else:
            computador_tira += 1
    return computador_tira

def campeonato():
    vez = 1
    while vez <= 3:
        print("****** Rodada: ", vez )
        rodada()
        vez += 1
    print("Você 0 x 3 Computador")

def rodada():
    n = 0

    while n <= 0:
        n = int(input("Quantas peças tera o jogo? "))
    m = n
    while m >= n or m <= 0:
        m = int(input("Quatas peças pode tirar?  "))

    vez_pc = False

    if n % (m + 1) == 0:
        print("Você comeca")
    else:
        print("Computador começa")
        vez_pc = True
    while n > 0:
        if vez_pc:
            computador_tira = computador_escolhe_jogada(n, m)
            n -= computador_tira
            if computador_tira == 1:
                print("Computador tirou uma peça ")
            else:
                print("computador tirou ", computador_tira, "peças")

            vez_pc = False
        else:
            tirar = usuario_escolhe_jogada(n, m)
            n -= tirar
            if tirar == 1:
                print("Você tirou uma peça ")
            else:
                print("Você tirou ", tirar, "peças" )

            vez_pc = True

            if n == 1:
                print("Resta uma peça")
            elif n != 0:

                print("Resta ", n, "peças")

    print("Fim de jogo!")



print("Bem vindo ao jogo Nim ")
jogo = " "
while jogo != "1" or  jogo != "2":
    jogo = input("Digite 1 para rodada unica ou 2 para campeonato: ")
    if jogo == "2":
        print("Você escolheu um campeonato")
        print("Vamos comecar?! ")
        campeonato()
    elif jogo == "1":
        print("Você escolheu uma rodada ")
        print("Vamos começar?! ")
        rodada()

    break
