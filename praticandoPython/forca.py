import random


def imprime_saudacao():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def carrega_palavra_secreta():
    arquivo = open("testo.txt", "w")
    arquivo.write("melancia\n")
    arquivo.write("maça\n")
    arquivo.write("bolacha\n")
    arquivo.write("banana\n")
    arquivo.close()
    arquivo = open("testo.txt", "r")
    palavras = []

    for linhas in arquivo:
        linhas = linhas.strip()
        palavra = palavras.append(linhas)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero]
    return palavra_secreta


def inicialize_letras_acertadas(palavra):

    return ["_" for letra in palavra]


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def jogar():

    imprime_saudacao()
    palavra_secreta = carrega_palavra_secreta()


    letras_acertadas = inicialize_letras_acertadas(palavra_secreta)#["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0
    while (not enforcou and not acertou):

        chute = input("Qual a letra?").strip().lower()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta.lower():
                if chute == letra:
                    letras_acertadas[index] = letra
                index +=1
        else:
            erros +=1
            desenha_forca(erros)
        enforcou = erros ==7
        acertou = "_" not in letras_acertadas

        print("letras acertadas: {}".format(letras_acertadas))

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)
if(__name__ == "__main__"):
    jogar()
