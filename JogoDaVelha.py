def print_tabuleiro(tabuleiro):
    # Função para imprimir o tabuleiro do jogo da velha
    for linha in tabuleiro:
        # Imprime cada linha do tabuleiro, unindo os elementos com " | "
        print(" | ".join(linha))
        # Imprime uma linha horizontal para separar as linhas do tabuleiro
        print("-" * 5)

def verificar_vitoria(tabuleiro, jogador):
    # Função para verificar se o jogador atual venceu
    # Verificar linhas
    for linha in tabuleiro:
        # Se todos os elementos na linha forem iguais ao símbolo do jogador, o jogador venceu
        if all(elemento == jogador for elemento in linha):
            return True

    # Verificar colunas
    for coluna in range(3):
        # Se todos os elementos na coluna atual forem iguais ao símbolo do jogador, o jogador venceu
        if all(tabuleiro[linha][coluna] == jogador for linha in range(3)):
            return True

    # Verificar diagonais
    if all(tabuleiro[i][i] == jogador for i in range(3)) or \
       all(tabuleiro[i][2-i] == jogador for i in range(3)):
        return True

    # Se nenhuma das condições acima for atendida, o jogador não venceu
    return False

def jogar_jogo_da_velha():
    # Função principal para jogar o jogo da velha
    # Inicializa o tabuleiro vazio
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    # Define o jogador inicial como 'X'
    jogador = 'X'

    # Mensagem de boas-vindas
    print("Bem-vindo ao Jogo da Velha!")
    # Imprime o tabuleiro inicial
    print_tabuleiro(tabuleiro)

    # Loop para cada jogada (máximo de 9 jogadas)
    for _ in range(9):
        # Solicita ao jogador as coordenadas da sua jogada
        linha = int(input(f"Jogador {jogador}, escolha a linha (0-2): "))
        coluna = int(input(f"Jogador {jogador}, escolha a coluna (0-2): "))

        # Verifica se a posição escolhida já foi ocupada
        if tabuleiro[linha][coluna] != " ":
            print("Essa posição já foi escolhida. Tente novamente.")
            continue

        # Atualiza o tabuleiro com a jogada do jogador atual
        tabuleiro[linha][coluna] = jogador
        # Imprime o tabuleiro atualizado
        print_tabuleiro(tabuleiro)

        # Verifica se o jogador atual venceu
        if verificar_vitoria(tabuleiro, jogador):
            print(f"Parabéns! Jogador {jogador} venceu!")
            return

        # Alterna para o próximo jogador
        jogador = 'O' if jogador == 'X' else 'X'

    # Se não houve vencedor após 9 jogadas, o jogo termina em empate
    print("Empate! O jogo terminou sem vencedores.")

# Chamada para iniciar o jogo da velha
jogar_jogo_da_velha()
