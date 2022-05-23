# Simular um jogo da mega-sena
# usuário escolher 5 números (0 a 60)
# o computador sortear 5 números
import random as r
import numpy as np

acertos = 0
numeros_iguais = []

def verify_chosen_numbers(numeros_escolhidos: list, qtd: int) -> None:
    if len(numeros_escolhidos) < qtd:
        print(f"Escolha {qtd} números não repetidos")
        return None

def gear_second(*n):
    global acertos

    numeros_escolhidos = set(n)
    verify_chosen_numbers(numeros_escolhidos, len(n))
    numero_vezes_necessarias = 0
    numeros_sorteados = set()

    while numeros_sorteados != numeros_escolhidos:
        todos_numeros = [i for i in range(0, 61)]
        numeros_sorteados = {todos_numeros.pop(r.randint(0, len(todos_numeros) - 1)) for _ in range(len(n))}
        numero_vezes_necessarias += 1

    print(numero_vezes_necessarias)


    numeros_acertados = list(numeros_escolhidos.intersection(numeros_sorteados))
    print("você acertou {} números, eles foram: {}. os números que você jogou foram: {} | números sorteados foram: {}".format(len(numeros_acertados), numeros_acertados, numeros_escolhidos, numeros_sorteados))

gear_second(1, 5, 6, 20)
















 # def player(a, b, c, d, e):
 #     global acertos
 #
 #     for i in range(5):
 #         #p = random.randrange(0, 61)
 #
 #         if a == p:
 #             acertos += 1
 #         elif b == p:
 #             acertos += 1
 #         elif c == p:
 #             acertos += 1
 #         elif d == p:
 #             acertos += 1
 #         elif e == p:
 #             acertos += 1
 #         print(p)
 #
 # print("ele acertou {} numeros".format(acertos))



