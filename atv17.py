import random  # Importa o módulo random para gerar números aleatórios

def main():
    print("Bem Vindo ao jogo de adivinhação!")  # Imprime uma mensagem de boas-vindas
    print("Tente adivinhar o número de 1 até 100.")  # Instrui o jogador sobre o intervalo de números

    numero_secreto = random.randint(1, 100)  # Gera um número aleatório entre 1 e 100
    tentativas = 0  # Inicializa o contador de tentativas

    while True:  # Loop infinito para continuar o jogo até que o jogador acerte o número
        try:
            tentativa = int(input("Digite a sua tentativa: "))  # Solicita ao jogador para digitar sua tentativa
            tentativas += 1  # Incrementa o contador de tentativas

            if tentativa == numero_secreto:  # Verifica se a tentativa é igual ao número secreto
                print(f"Parabéns! Você acertou o número secreto {numero_secreto} em {tentativas} tentativas.")
                # Imprime uma mensagem de parabéns com o número secreto e o número de tentativas
                break  # Sai do loop, encerrando o jogo

            elif tentativa < numero_secreto:  # Verifica se a tentativa é menor que o número secreto
                print("Tente achar um número maior.")  # Informa ao jogador para tentar um número maior

            else:  # Se não for igual nem menor, só pode ser maior
                print("Tente achar um número menor.")  # Informa ao jogador para tentar um número menor

        except ValueError:  # Captura uma exceção se o jogador digitar algo que não seja um número
            print("Por favor, digite um número válido.")  # Informa ao jogador para digitar um número válido

if __name__ == "__main__":
    main()  # Chama a função main() quando o script é executado diretamente

