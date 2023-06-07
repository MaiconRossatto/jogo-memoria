import random
import time
import os

board = []
found_pairs = []
point = 1000

def cleanTerminal1():
    os.system('cls' if os.name == 'nt' else 'clear')

def cleanTerminal2():
    i = input("")
    os.system('cls' if os.name == 'nt' else 'clear')

def tabuleiro():
    emojis = ['🐶', '🐺', '🦁', '🐸', '🐼', '🐔', '🐳', '🦖', '🦉', '🐞', '🐷', '🦄']
    random.shuffle(emojis)
    pairs = emojis[:6] * 2
    random.shuffle(pairs)
    board = [[' ' for _ in range(4)] for _ in range(3)]

    for i in range(3):
        for j in range(4):
            index = i * 4 + j
            board[i][j] = (pairs[index], (i, j))

    return board

def print_board(board, show_all=False):
    print("   |  0  |  1  |  2  |  3")
    print("--------------------------")
    for i in range(3):
        print(f"{i}  | ", end='')
        for j in range(4):
            emoji, coord = board[i][j]
            if show_all or coord in found_pairs:
                print(f"{emoji}  | ", end='')
            else:
                print("   | ", end='')
        print()

def save_score(name, score):
    with open("ranking.txt", "a") as file:
        file.write(f"{name}: {score}\n")

def show_ranking():
    if os.path.exists("ranking.txt"):
        with open("ranking.txt", "r") as file:
            ranking = file.readlines()
            if ranking:
                print("Ranking:")
                for line in ranking:
                    name, score = line.strip().split(":")
                    print(f"Nome: {name}, Pontuação: {score}")
            else:
                print("Nenhum ranking encontrado.")
    else:
        print("Nenhum ranking encontrado.")

def newGame(name):
    global board, found_pairs, point
    print("######TABULEIRO########")
    board = tabuleiro()
    print_board(board, show_all=True)
    time.sleep(10)
    cleanTerminal1()
    found_pairs = []
    point = 1000
    print("O jogo começou!\n")
    print_board(board)

    emojis = ['🐶', '🐺', '🦁', '🐸', '🐼', '🐔', '🐳', '🦖', '🦉', '🐞', '🐷', '🦄']
    num_pairs = len(emojis)

    while len(found_pairs) < num_pairs:
        print(f"\nPontuação atual: {point}\n")
        print("\n### Informe as coordenadas da primeira Imagem:\n")
        try:
            opc1_coluna = int(input("Informe a Coluna: "))
            opc1_linha = int(input("Informe a Linha: "))

            print("\n### Informe as coordenadas da segunda Imagem:\n")
            opc2_coluna = int(input("Informe a Coluna: "))
            opc2_linha = int(input("Informe a Linha: "))

            if (
                opc1_coluna < 0 or opc1_coluna > 3 or
                opc1_linha < 0 or opc1_linha > 2 or
                opc2_coluna < 0 or opc2_coluna > 3 or
                opc2_linha < 0 or opc2_linha > 2
            ):
                print("Coordenadas inválidas! Tente novamente.")
                continue

            emoji1, coord1 = board[opc1_linha][opc1_coluna]
            emoji2, coord2 = board[opc2_linha][opc2_coluna]

            if emoji1 == emoji2:
                cleanTerminal1()
                print("Par correspondente encontrado!")
                found_pairs.append(coord1)
                found_pairs.append(coord2)
                print_board(board)
            else:
                cleanTerminal1()
                print("As coordenadas selecionadas não formam um par:")
                print(f"Coordenada 1: {coord1}, Emoji: {emoji1}")
                print(f"Coordenada 2: {coord2}, Emoji: {emoji2}")
                print("Tentando novamente...")
                print()
                point -= 50
                print_board(board)

        except (ValueError, IndexError):
            print("Coordenadas inválidas! Tente novamente.")

    if len(found_pairs) == num_pairs:
        print("Parabéns! Você encontrou todos os pares!")
        save_score(name, point)
    else:
        print("Jogo encerrado. Tente novamente!")

def main():
    print("### Bem-vindo ao jogo da memória ###\n")

    menu = True

    while menu:
        print("[1] Começar a Jogar:")
        print("[2] Ver Ranking:")
        print("[3] Sair")
        try:
            menu = int(input("Valor: "))
            cleanTerminal1()

            if menu == 3:
                menu = False
            elif menu == 1:
                print("Novo Jogo")
                name = input("Informe o seu nome: ")
                cleanTerminal1()
                newGame(name)
            elif menu == 2:
                show_ranking()
                cleanTerminal2()
        except ValueError:
            print("\nValor inválido!!")

main()
