def print_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 5)

def verificar_vitoria(tabuleiro, jogador):
    # Verificar linhas
    for linha in tabuleiro:
        if all(elemento == jogador for elemento in linha):
            return True

    # Verificar colunas
    for coluna in range(3):
        if all(tabuleiro[linha][coluna] == jogador for linha in range(3)):
            return True

    # Verificar diagonais
    if all(tabuleiro[i][i] == jogador for i in range(3)) or \
       all(tabuleiro[i][2-i] == jogador for i in range(3)):
        return True

    return False

def jogar_jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador = 'X'

    print("Bem-vindo ao Jogo da Velha!")
    print_tabuleiro(tabuleiro)

    for _ in range(9):
        linha = int(input(f"Jogador {jogador}, escolha a linha (0-2): "))
        coluna = int(input(f"Jogador {jogador}, escolha a coluna (0-2): "))

        if tabuleiro[linha][coluna] != " ":
            print("Essa posição já foi escolhida. Tente novamente.")
            continue

        tabuleiro[linha][coluna] = jogador
        print_tabuleiro(tabuleiro)

        if verificar_vitoria(tabuleiro, jogador):
            print(f"Parabéns! Jogador {jogador} venceu!")
            return

        jogador = 'O' if jogador == 'X' else 'X'

    print("Empate! O jogo terminou sem vencedores.")

jogar_jogo_da_velha()
